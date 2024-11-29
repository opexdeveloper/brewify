from typing import List, Optional, Any, Union, Dict
from pydantic import BaseModel, RootModel

class CreditsModel(BaseModel):
    director: Optional[str]
    writer: Optional[str]
    cast: Optional[List[str]]

class InformationModel(BaseModel):
    country: Optional[str]
    released: Optional[str]
    runtime: Optional[str]
    rated: Optional[str]
    genre: Optional[str]
    series: Optional[Union[Dict[str, Any], bool]]

class ImdbSearchResponseModel(BaseModel):
    """`imdb` response model"""
    url: Optional[str]
    title: Optional[str]
    plot: Optional[str]
    poster: Optional[str]
    credits: CreditsModel
    information: InformationModel
    rating: Optional[float]
    ratings: Optional[List[Dict[str, Any]]]