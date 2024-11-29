from pydantic import BaseModel
from typing import Optional

class TextSearchResponse(BaseModel):
    """`google text` response model"""
    title: Optional[str]
    link: Optional[str]
    snippet: Optional[str]