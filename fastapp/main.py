from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .config import settings
from .api.v1.api import file_router, text_router

app = FastAPI(
    title=settings.title,
    description=settings.description,
)

# # v1
# app.include_router(file_router, tags=["v1"])
# app.include_router(text_router, tags=["v1"])
app.include_router(text_router, tags=["v2"])


@app.get("/")
async def root():
    return RedirectResponse("/docs", status_code=301)
