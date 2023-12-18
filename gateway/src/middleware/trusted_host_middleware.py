from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from src.settings.trusted_host_settings import TrustedHostSettings


class TrustedHostMiddlewareConfig:
    def __init__(
        self, app: FastAPI, trusted_host_settings: TrustedHostSettings
    ) -> None:
        self.app: FastAPI = app
        self.trusted_host_settings: TrustedHostSettings = trusted_host_settings

    def add_trusted_host_middleware(self) -> None:
        self.app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=self.trusted_host_settings.allowed_hosts,
        )
