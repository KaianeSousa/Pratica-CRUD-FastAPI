from pydantic import BaseModel


class Auth(BaseModel):
    email: str
    senha: str