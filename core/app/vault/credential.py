from dataclasses import dataclass


@dataclass
class Credential:
    id: str
    name: str
    credential_type: str
    username: str
    secret: str
