from pydantic import Field, model_validator
from pydantic_settings import BaseSettings


class ApiSettings(BaseSettings):
    title: str = Field(default='API', alias='API_TITLE')
    description: str = Field(default='', alias='API_DESCRIPTION')
    version: str = Field(default='0.0.0', alias='API_VERSION')
    docs_url: str | None = Field(default='/docs', alias='API_DOCS_URL')
    redocs_url: str | None = Field(default='/redoc', alias='API_REDOCS_URL')
    prefix: str = Field(default='/api', alias='API_PREFIX')
