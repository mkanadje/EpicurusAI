from backend import ROOT_PATH
from pydantic_settings import BaseSettings
from functools import lru_cache
import os


class Settings(BaseSettings):
    UPLOAD_FOLDER: str = os.path.join(ROOT_PATH, "..", "data", "uploads")


@lru_cache
def get_settings() -> Settings:
    return Settings()
