from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.connectors.ssh_connector import SSHConnector
from app.database.session import get_db
from app.schemas.assets import Asset, AssetCreate
from app.schemas.ssh import SSHDiscoveryRequest
from app.services.asset_registry import asset_registry
from app.vault.service import vault_service

router = APIRouter(prefix="/connectors/ssh", tags=["connectors"])


@router.post("/discover", response_model=Asset)
async def discover_linux_host(
    payload: SSHDiscoveryRequest,
    db: Session = Depends(get_db),
):
    credential = vault_service.get(db, payload.credential_id)

    if credential is None:
        raise HTTPException(status_code=404, detail="Credential not found")

    connector = SSHConnector()

    try:
        metadata = connector.discover(
            host=payload.host,
            username=credential.username,
            password=credential.secret,
            port=payload.port,
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"SSH discovery failed: {exc}")

    asset_payload = AssetCreate(
        asset_type="linux_server",
        display_name=metadata.get("hostname") or payload.host,
        organization_id=payload.organization_id,
        site_id=payload.site_id,
        metadata=metadata,
    )

    return await asset_registry.create_asset(db, asset_payload)
