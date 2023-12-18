from pydantic import BaseModel


class DBAccount(BaseModel):
    name: str
    password: str
    role: str = 'User'
