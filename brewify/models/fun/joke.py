from pydantic import BaseModel

class Joke(BaseModel):
    """`joke` response model"""
    setup: str
    punchline: str