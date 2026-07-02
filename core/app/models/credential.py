from sqlalchemy import String, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from app.database.session import Base


class CredentialModel(Base):
    __tablename__ = "credentials"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)

    # encrypted fields (NEVER stored in plaintext)
    encrypted_username: Mapped[bytes] = mapped_column(LargeBinary)
    encrypted_secret: Mapped[bytes] = mapped_column(LargeBinary)

    credential_type: Mapped[str] = mapped_column(String, index=True)
