from fastapi import FastAPI
from .settings import Settings
from ..vector_db.mongo_client import MongoClientManager

class AppServer:
    def __init__(self):
        self._settings = Settings()
        self._app = FastAPI(title="Book-RAG API")
        self._client = MongoClientManager(
            uri=self._settings.mongodb_uri,
            db_name=self._settings.mongodb_db,
        )
        self._register_events()
        self._register_routes()

    @property
    def app(self) -> FastAPI:
        return self._app

    def _register_events(self):
        @self._app.on_event("startup")
        async def startup():
            await self._client.connect()
            self._app.state.db = self._client.database()

        @self._app.on_event("shutdown")
        async def shutdown():
            await self._client.close()

    def _register_routes(self):
        @self._app.get("/health")
        async def health():
            return {"status": "ok"}
