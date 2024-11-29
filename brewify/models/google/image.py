from pydantic import BaseModel
from typing import Optional

class ImageLinkResponse(BaseModel):
    """`google image` response model"""
    link: Optional[str]