import base64
import hashlib
from uuid import uuid4

from cryptography.fernet import Fernet
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.credential import CredentialModel
from app.schemas.vault import CredentialCreate, CredentialMetadata
from app.vault.credential import Credential


class VaultService:

    def __init__(self):
        key = hashlib.sha256(settings.vault_key.encode()).digest()
        self.fernet = Fernet(base64.urlsafe_b64encode(key))

    # -------------------------
    # CREATE
    # -------------------------
    def create_credential(self, db: Session, payload: CredentialCreate):

        encrypted_username = self.fernet.encrypt(
            payload.username.encode()
        )

        encrypted_secret = self.fernet.encrypt(
            payload.password.encode()
        )

        model = CredentialModel(
            id=f"cred_{uuid4().hex}",
            name=payload.name,
            credential_type=payload.credential_type,
            encrypted_username=encrypted_username,
            encrypted_secret=encrypted_secret,
        )

        db.add(model)
        db.commit()
        db.refresh(model)

        return self._to_metadata(model)

    # -------------------------
    # LIST (NO SENSITIVE DATA)
    # -------------------------
    def list_credentials(self, db: Session):
        return [
            self._to_metadata(c)
            for c in db.query(CredentialModel).all()
        ]

    # -------------------------
    # GET FULL CREDENTIAL (INTERNAL ONLY)
    # -------------------------
    def get(self, db: Session, credential_id: str) -> Credential | None:

        model = (
            db.query(CredentialModel)
            .filter(CredentialModel.id == credential_id)
            .first()
        )

        if not model:
            return None

        username = self.fernet.decrypt(model.encrypted_username).decode()
        secret = self.fernet.decrypt(model.encrypted_secret).decode()

        return Credential(
            id=model.id,
            name=model.name,
            credential_type=model.credential_type,
            username=username,
            secret=secret,
        )

    # -------------------------
    # PUBLIC SAFE VIEW
    # -------------------------
    def _to_metadata(self, model: CredentialModel):
        return CredentialMetadata(
            id=model.id,
            name=model.name,
            credential_type=model.credential_type,
        )


vault_service = VaultService()
