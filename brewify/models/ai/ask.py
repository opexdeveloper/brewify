from pydantic import BaseModel

class Ask(BaseModel):
    """`chatbot` response model"""
    response: str