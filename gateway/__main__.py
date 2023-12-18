import dotenv
from server.server_main import Server
from server.server_settings import ServerSettings


def main() -> None:
    dotenv.load_dotenv()
    settings: ServerSettings = ServerSettings()
    server: Server = Server(settings=settings)
    server.run()


if __name__ == '__main__':
    main()
