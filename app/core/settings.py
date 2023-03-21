from pathlib import Path

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    ...

    class Config:
        env_file = "./.env"


settings = Settings()

BASE_DIR = Path(__file__).resolve().parent.parent
