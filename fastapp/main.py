from functools import lru_cache

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# from fastapp.config import settings
from fastapp.api.v2.api import subway_router
from fastapp.core.settings import get_settings


settings = get_settings()
app = FastAPI(
    title=settings.title,
    description=settings.description,

)

# # v1
# app.include_router(file_router, tags=["v1"])
# app.include_router(text_router, tags=["v1"])
app.include_router(subway_router, tags=["v2"])
# app.include_router(ui_router, tags=["v2"])
# https://github.com/tiangolo/sqlmodel

@app.get("/")
async def root():
    return RedirectResponse("/docs", status_code=301)
