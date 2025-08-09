import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:password@localhost:5432/auth_db")
    secret_key: str = os.getenv("SECRET_KEY", "secretkey")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
