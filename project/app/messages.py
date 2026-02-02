from enum import Enum
from typing import Any

class MessageKey(Enum):
    HEALTH_OK = "HEALTH_OK"
    DB_CONNECTED = "DB_CONNECTED"
    DB_CONNECTION_FAILED = "DB_CONNECTION_FAILED"
    FILE_UPLOADED = "FILE_UPLOADED"
    INGESTION_SUCCESS = "INGESTION_SUCCESS"
    INGESTION_FAILED = "INGESTION_FAILED"
    CHUNK_SAVED = "CHUNK_SAVED"
    INVALID_INPUT = "INVALID_INPUT"

class Messages:
    HEALTH_OK = "ok"
    DB_CONNECTED = "Connected to database"
    DB_CONNECTION_FAILED = "Database connection failed"
    FILE_UPLOADED = "File uploaded: {filename}"
    INGESTION_SUCCESS = "Document ingested successfully"
    INGESTION_FAILED = "Document ingestion failed"
    CHUNK_SAVED = "Chunk saved: {chunk_id}"
    INVALID_INPUT = "Invalid input"

    @classmethod
    def get(cls, key: MessageKey) -> str:
        return getattr(cls, key.value)

    @classmethod
    def format(cls, key: MessageKey, **kwargs: Any) -> str:
        return cls.get(key).format(**kwargs)
