from pydantic import BaseModel
from typing import List, Optional

class Guild(BaseModel):
    id: str
    name: str
    splash: Optional[str]
    banner: Optional[str]
    description: Optional[str]
    icon: Optional[str]
    features: List[str]
    verification_level: int
    vanity_url_code: Optional[str]
    nsfw_level: int
    nsfw: bool
    premium_subscription_count: Optional[int]


class Channel(BaseModel):
    id: str
    type: int
    name: str

class Model(BaseModel):
    """`discord guild` response model"""
    type: int
    code: str
    expires_at: Optional[str]
    guild: Guild
    guild_id: str
    channel: Optional[Channel]