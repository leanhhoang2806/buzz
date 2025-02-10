from pydantic import BaseModel

class Suggestion(BaseModel):
    name: str
    latitude: float
    longitude: float
    score: float