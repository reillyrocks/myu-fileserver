from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# from fastapp.config import settings
# from .api.v1.api import file_router, text_router
from fastapp.api.v2.api import subway_router

app = FastAPI(
    title="MYU API",
    description="API for interacting with anything",
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
