from pydantic import BaseSettings


class Settings(BaseSettings):
    title = "MYU API"
    description = "API for interacting with anything"

    class Config:
        case_sensitive = True


settings = Settings()
