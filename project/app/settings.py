from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    mongodb_uri: str = Field(default="mongodb://mongo:27017")
    mongodb_db: str = Field(default="bookrag")
    app_host: str = Field(default="0.0.0.0")
    app_port: int = Field(default=8000)
