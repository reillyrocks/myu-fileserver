from pathlib import Path

from fastapi import UploadFile

from fastapp.api.v1.schema import File
import subprocess as sb

STORAGE_PATH = "/home"

# file_name: location
files = {}


async def list_files():
    return files.keys()


async def get_file(file_name: str):
    with open(files[file_name]) as read_file:
        return read_file


async def post_file(file: UploadFile):
    await add_file_to_posix(file)
    return True


async def add_file_to_posix(file: UploadFile):
    if Path(STORAGE_PATH + file.filename).exists():
        return False
    contents = await file.read()
    with open(Path(STORAGE_PATH + file.filename), 'wb') as savefile:
        savefile.write(contents)
        files[file.filename] = Path(STORAGE_PATH + file.filename)
