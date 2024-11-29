from pydantic import BaseModel, HttpUrl
from typing import Optional, Any

class AvatarDecorationData(BaseModel):
    asset: Optional[str]  
    sku_id: Optional[str]  
    expires_at: Optional[Any] 

class UserInfoResponse(BaseModel):
    """`discord user` response model"""
    id: str
    username: str
    discriminator: str
    public_flags: int
    flags: int
    accent_color: int
    global_name: Optional[str]
    avatar_decoration_data: Optional[AvatarDecorationData]  
    banner_color: str
    clan: Optional[str]
    avatar: HttpUrl