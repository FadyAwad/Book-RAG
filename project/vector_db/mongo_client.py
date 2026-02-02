from motor.motor_asyncio import AsyncIOMotorClient

class MongoClientManager:
    def __init__(self, uri: str, db_name: str):
        self._uri = uri
        self._db_name = db_name
        self._client: AsyncIOMotorClient | None = None

    async def connect(self):
        self._client = AsyncIOMotorClient(self._uri)

    async def close(self):
        if self._client:
            self._client.close()
            self._client = None

    def database(self):
        if not self._client:
            raise RuntimeError("Mongo client not initialized")
        return self._client[self._db_name]
