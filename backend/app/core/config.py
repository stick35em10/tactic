from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # DATABASE_URL: str = "postgresql+psycopg2://user:password@localhost/tactic_db"
    DATABASE_URL: str = "sqlite:////home/stick35em10/tactic/data/tactic.db"
    SECRET_KEY: str = "a_very_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
