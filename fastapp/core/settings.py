import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
import pathlib


def load_settings():
    if os.getenv("TESTING", "false").lower() == "true":
        return SettingsConfigDict(secrets_dir='/run/secrets')
    else:
        parent_dir = pathlib.Path(__file__).parent.parent
        return SettingsConfigDict(env_file=f'{parent_dir}/tests/test_env')


class Settings(BaseSettings):
    model_config = load_settings()

    title: str = "MYU App"
    description: str = "API for interacting with anything"
    secret_key: str


@lru_cache
def get_settings():
    return Settings()