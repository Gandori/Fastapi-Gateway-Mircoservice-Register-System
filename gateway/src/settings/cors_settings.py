from pydantic import Field
from pydantic_settings import BaseSettings


class CorsSettings(BaseSettings):
    allow_origins: str = Field(default='*', alias='CORS_ALLOW_ORIGINS')
    allow_credentials: bool = Field(default=True, alias='CORS_ALLOW_CREDENTIALS')
    allow_methods: str = Field(default='*', alias='CORS_ALLOW_METHODS')
    allow_headers: str = Field(default='*', alias='CORS_ALLOW_HEADERS')
