from motor.core import AgnosticCollection, AgnosticCursor, AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError

from src.database.exceptions import (
    DatabaseCreateIndexError,
    DatabaseDeleteError,
    DatabaseDropError,
    DatabaseDropIndexError,
    DatabaseDuplicateKeyError,
    DatabaseFindError,
    DatabaseInsertError,
    DatabaseUpdateError,
)
from src.database.settings import DatabaseSettings
from src.models.index import Index


class Database:
    def __init__(self, settings: DatabaseSettings) -> None:
        self.settings: DatabaseSettings = settings
        self.client: AgnosticDatabase = AsyncIOMotorClient(self.settings.url).college
        self.collection: str = self.settings.collection

    async def find(self, where: dict = {}, skip: int = 0, limit: int = 25) -> list:
        try:
            cursor: AgnosticCursor = self.client[self.collection].find(where)
            return await cursor.skip(skip=skip).to_list(length=limit)
        except Exception as e:
            raise DatabaseFindError(e)

    async def find_one(self, where: dict) -> dict:
        try:
            result: None = await self.client[self.collection].find_one(where)
            if not result:
                raise DatabaseFindError()
            return result
        except Exception as e:
            raise DatabaseFindError(e)

    async def insert_many(self, documents: list[dict]) -> None:
        try:
            await self.client[self.collection].insert_many(documents)
        except Exception as e:
            raise DatabaseInsertError(e)

    async def insert_one(self, document: dict) -> None:
        try:
            await self.client[self.collection].insert_one(document)
        except DuplicateKeyError as e:
            raise DatabaseDuplicateKeyError(e)
        except Exception as e:
            raise DatabaseInsertError(e)

    async def update_one_set(self, where: dict, row: dict) -> None:
        try:
            await self.client[self.collection].update_one(where, {'$set': row})
        except Exception as e:
            raise DatabaseUpdateError(e)

    async def update_one_inc(self, where: dict, row: dict) -> None:
        try:
            await self.client[self.collection].update_one(where, {'$set': row})
        except Exception as e:
            raise DatabaseUpdateError(e)

    async def update_many_set(self, where: dict, update: dict[str, str]) -> None:
        try:
            collection: AgnosticCollection = self.client[self.collection]
            await collection.update_many(where, update={'$set': update})
        except Exception as e:
            raise DatabaseUpdateError(e)

    async def update_many_inc(self, where: dict, update: dict[str, int]) -> None:
        try:
            collection: AgnosticCollection = self.client[self.collection]
            await collection.update_many(where, update={'$inc': update})
        except Exception as e:
            raise DatabaseUpdateError(e)

    async def delete_one(self, where: dict) -> None:
        try:
            await self.client[self.collection].delete_one(where)
        except Exception as e:
            raise DatabaseDeleteError(e)

    async def delete_many(self, where: dict) -> None:
        try:
            await self.client[self.collection].delete_many(where)
        except Exception as e:
            raise DatabaseDropError(e)

    async def create_index(self, index: Index) -> None:
        options: dict = {
            "name": index.name,
            "unique": index.unique,
            "expireAfterSeconds": index.expireAfterSeconds,
            "sparse": index.sparse,
        }
        collection: AgnosticCollection = self.client[self.collection]

        try:
            await collection.create_index(keys=[(index.index, index.sort)], **options)
        except Exception as e:
            raise DatabaseCreateIndexError(e)

    async def drop_index(self, index: str) -> None:
        try:
            await self.client[self.collection].drop_index(index_or_name=index)
        except Exception as e:
            raise DatabaseDropIndexError(e)

    async def drop_collection(self) -> None:
        try:
            await self.client[self.collection].drop()
        except Exception as e:
            raise DatabaseDropError(e)
