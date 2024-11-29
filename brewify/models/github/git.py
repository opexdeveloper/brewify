from pydantic import BaseModel, HttpUrl
from typing import List, Optional



class Repository(BaseModel):
    url: HttpUrl
    name: str
    description: Optional[str] = None
    language: Optional[str] = None
    created: str  


class Location(BaseModel):
    name: Optional[str] = None
    url: Optional[HttpUrl] = None

class Connections(BaseModel):
    email: Optional[str] = None
    twitter: Optional[str] = None
    website: Optional[HttpUrl] = None

class UserProfile(BaseModel):
    id: int
    url: HttpUrl
    name: str
    username: Optional[str] = None
    avatar: HttpUrl
    bio: Optional[str] = None
    created: str  
    location: Optional[Location] = None
    company: Optional[str] = None
    connections: Connections


class GitHubResponse(BaseModel):
    user: UserProfile
    repositories: List[Repository]