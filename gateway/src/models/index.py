from pydantic import BaseModel


class Index(BaseModel):
    index: str
    name: str
    sort: int = 1
    unique: bool = False
    expireAfterSeconds: int | None = None
    sparse: bool = True
