from enum import Enum
from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel


# I will eventually set up a "garbage" collector. Something that cleans up over time
class LifeSpan(str, Enum):
    short = "short"
    long = "long"
    permanent = "permanent"


class Item(BaseModel):
    name: str
    long_term: Optional[LifeSpan] = LifeSpan.short


class File(Item):
    item: Optional[UploadFile]


class Text(Item):
    text_field: str
