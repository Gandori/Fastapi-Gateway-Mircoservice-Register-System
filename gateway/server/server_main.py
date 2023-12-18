import uvicorn
from server.server_settings import ServerSettings


class Server:
    def __init__(self, settings: ServerSettings) -> None:
        self.settings: ServerSettings = settings

    def run(self) -> None:
        uvicorn.run(app='src:app', **self.settings.dict())
