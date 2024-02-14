from enum import Enum
from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    message: str

class Languages(str, Enum):
    b = "b"
    c = "c"
    python = "python"
    java = "java"
    javascript = "javascript"


class Programmer(BaseModel):
    id: int
    name: str
    languages: List[Languages]
