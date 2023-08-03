from pydantic import BaseSettings


class Settings(BaseSettings):
    title = "MYU API"
    description = "API for interacting with filesystem/api to act as a fileserver to store links, images, files"

    class Config:
        case_sensitive = True


settings = Settings()
