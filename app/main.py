from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from . import schema, service
app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs", status_code=301)


@app.post("/post_text")
async def post_text(request: schema.Text) -> bool:
    return service.post_text(request)


@app.post("/post_file")
async def post_file(request: schema.File) -> bool:
    return service.post_file(request)


@app.get("/get_file/{file_name}")
async def get_file(file_name: str) -> str:
    return service.get_file(file_name)


@app.get("/list_text")
async def list_text() -> list[str]:
    return service.list_text()


@app.get("/list_files()")
async def list_files() -> list[str]:
    return service.list_files()
