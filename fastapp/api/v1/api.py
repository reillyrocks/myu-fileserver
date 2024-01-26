from fastapi import APIRouter, UploadFile

from . import schema
from .services import texts, files

file_router = APIRouter(
    prefix="/files",
)


@file_router.post("/post_file")
async def post_file(file: UploadFile) -> bool:
    return await files.post_file(file)


@file_router.get("/get_file/{file_name}")
async def get_file(file_name: str) -> str:
    return await files.get_file(file_name)


@file_router.get("/list_files()")
async def list_files() -> list[str]:
    return files.list_files()


text_router = APIRouter(
    prefix="/text",
)

@text_router.post("/post_text")
async def post_text(request: schema.Text) -> bool:
    return texts.post_text(request)

@text_router.get("/list_text")
async def list_text() -> list[str]:
    return texts.list_text()

