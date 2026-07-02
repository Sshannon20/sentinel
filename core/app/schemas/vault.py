from pydantic import BaseModel


class CredentialCreate(BaseModel):
    name: str
    username: str
    password: str
    credential_type: str = "ssh_password"


class CredentialMetadata(BaseModel):
    id: str
    name: str
    credential_type: str
