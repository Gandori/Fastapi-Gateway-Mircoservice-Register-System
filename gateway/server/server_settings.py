from pydantic import Field
from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    host: str = Field(default='localhost', alias='SERVER_HOST')
    port: int = Field(default=10000, alias='SERVER_PORT')
    log_level: str = Field(default='info', alias='SERVER_LOG_LEVEL')
    reload: bool = Field(default=False, alias='SERVER_RELOAD')
    workers: int = Field(default=1, alias='SERVER_WORKERS')
    backlog: int = Field(default=2048, alias='SERVER_BACKLOCK')
    timeout_keep_alive: int = Field(default=5, alias='SERVER_TIMEOUT_KEEP_ALIVE')
    server_header: bool = Field(default=False, alias='SERVER_HEADER')
    date_header: bool = Field(default=False, alias='SERVER_DATE_HEADER')
