from pydantic import Field
from pydantic_settings import BaseSettings


class TrustedHostSettings(BaseSettings):
    allowed_hosts: str = Field(default='*', alias='ALLOWED_HOSTS')
