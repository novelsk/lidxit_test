import logging
from pathlib import Path

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
logging.warning(str(BASE_DIR.parent.joinpath('.env')))
load_dotenv(str(BASE_DIR.parent.joinpath('.env')))


class Settings(BaseSettings):
    MONGO_DB_URI: str
    PREFIX: str = ''

    class Config:
        env_file = str(BASE_DIR.parent.joinpath('.env'))


settings = Settings()
