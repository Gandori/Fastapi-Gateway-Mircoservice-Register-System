from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.settings.cors_settings import CorsSettings


class CorsMiddlewareConfig:
    def __init__(self, app: FastAPI, cors_settings: CorsSettings) -> None:
        self.app: FastAPI = app
        self.settings: CorsSettings = cors_settings

    def add_cors_middleware(self) -> None:
        self.app.add_middleware(CORSMiddleware, **self.settings.dict())
