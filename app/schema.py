from enum import Enum
from typing import Optional

from pydantic import BaseModel


class LifeSpan(str, Enum):
    short = "short"
    long = "long"
    permanent = "permanent"


class Item(BaseModel):
    name: str
    long_term: Optional[LifeSpan] = LifeSpan.short


class File(Item):
    location: Optional[str]


class Text(Item):
    text_field: str
