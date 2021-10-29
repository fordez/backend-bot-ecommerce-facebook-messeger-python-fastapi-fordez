from typing import Any, List
from pydantic import BaseModel


class DataRequest(BaseModel):
    object: str
    entry: List = []
