import os
from importlib.util import spec_from_file_location
from typing import Any

from fastapi import FastAPI
from src.middleware.cors_middleware import CorsMiddlewareConfig
from src.middleware.trusted_host_middleware import TrustedHostMiddlewareConfig
from src.settings.api_settings import ApiSettings
from src.settings.cors_settings import CorsSettings
from src.settings.trusted_host_settings import TrustedHostSettings

api_settings: ApiSettings = ApiSettings()
cors_settings: CorsSettings = CorsSettings()
trusted_host_settings: TrustedHostSettings = TrustedHostSettings()


openapi_url: str = f'{api_settings.prefix}/openapi.json'
app: FastAPI = FastAPI(**api_settings.dict(), openapi_url=openapi_url)

cors_middleware: CorsMiddlewareConfig = CorsMiddlewareConfig(
    app=app, cors_settings=cors_settings
)
trusted_host_middleware: TrustedHostMiddlewareConfig = TrustedHostMiddlewareConfig(
    app=app, trusted_host_settings=trusted_host_settings
)

cors_middleware.add_cors_middleware()
trusted_host_middleware.add_trusted_host_middleware()


def add_endpoint(endpoints_folder: str, prefix: str, file: str) -> None:
    ignore_files: list = ['__init__.py', '__pycache__']
    name: Any = file.replace('.py', '') if file not in ignore_files else None
    location: Any = f'{endpoints_folder}/{name}.py' if name else None
    spec: Any = spec_from_file_location(name=name, location=location) if name else None
    loader: Any = spec.loader if spec else None
    module: Any = loader.load_module() if loader else None
    router: Any = module.router if module else None
    app.include_router(router=router, prefix=prefix) if router else None


@app.on_event('startup')
async def startup() -> None:
    endpoints_folder: str = 'src/endpoints'
    prefix: str = api_settings.prefix
    for file in os.listdir(endpoints_folder):
        add_endpoint(endpoints_folder=endpoints_folder, prefix=prefix, file=file)
