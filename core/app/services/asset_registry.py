from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.asset import AssetModel
from app.schemas.assets import Asset, AssetCreate
from app.services.event_bus import SentinelEvent, event_bus


class AssetRegistry:
    async def create_asset(self, db: Session, payload: AssetCreate) -> Asset:
        existing = self._find_existing_asset(db, payload)

        if existing is not None:
            existing.asset_type = payload.asset_type
            existing.display_name = payload.display_name
            existing.organization_id = payload.organization_id
            existing.site_id = payload.site_id
            existing.asset_metadata = payload.metadata

            db.commit()
            db.refresh(existing)

            asset = self._to_schema(existing)

            await event_bus.publish(
                SentinelEvent(
                    type="asset.updated",
                    source="asset_registry",
                    data=asset.model_dump(),
                )
            )

            return asset

        model = AssetModel(
            id=f"asset_{uuid4().hex}",
            asset_type=payload.asset_type,
            display_name=payload.display_name,
            organization_id=payload.organization_id,
            site_id=payload.site_id,
            asset_metadata=payload.metadata,
        )

        db.add(model)
        db.commit()
        db.refresh(model)

        asset = self._to_schema(model)

        await event_bus.publish(
            SentinelEvent(
                type="asset.discovered",
                source="asset_registry",
                data=asset.model_dump(),
            )
        )

        return asset

    def list_assets(self, db: Session) -> list[Asset]:
        return [self._to_schema(model) for model in db.query(AssetModel).all()]

    def get_asset(self, db: Session, asset_id: str) -> Asset | None:
        model = db.query(AssetModel).filter(AssetModel.id == asset_id).first()

        if model is None:
            return None

        return self._to_schema(model)

    def _find_existing_asset(
        self,
        db: Session,
        payload: AssetCreate,
    ) -> AssetModel | None:
        ip = payload.metadata.get("ip")
        hostname = payload.metadata.get("hostname")

        existing_assets = (
            db.query(AssetModel)
            .filter(AssetModel.organization_id == payload.organization_id)
            .all()
        )

        for asset in existing_assets:
            metadata = asset.asset_metadata or {}

            if ip and metadata.get("ip") == ip:
                return asset

            if hostname and metadata.get("hostname") == hostname:
                return asset

        return None

    def _to_schema(self, model: AssetModel) -> Asset:
        return Asset(
            id=model.id,
            asset_type=model.asset_type,
            display_name=model.display_name,
            organization_id=model.organization_id,
            site_id=model.site_id,
            state=model.state,
            health=model.health,
            metadata=model.asset_metadata or {},
        )


asset_registry = AssetRegistry()
