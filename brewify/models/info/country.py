from typing import List
from pydantic import BaseModel

class CountryInfoResponse(BaseModel):
    country: str
    currency: str
    population: int
    languages: List[str]