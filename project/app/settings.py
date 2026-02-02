from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    mongodb_uri: str = Field(default="mongodb://mongo:27017")
    mongodb_db: str = Field(default="bookrag")
    app_host: str = Field(default="0.0.0.0")
    app_port: int = Field(default=8000)

    class Config:
        env_prefix = ""
