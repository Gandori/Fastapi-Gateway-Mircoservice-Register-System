from pydantic import BaseModel, ConfigDict


class SignInError(BaseModel):
    status_code: int = 500
    detail: str = (
        'Ihr Account konnte nicht angemeldet werden, versuchen sie es noch mal'
    )

    model_config: ConfigDict = {"json_schema_extra": {"examples": [{'detail': detail}]}}
