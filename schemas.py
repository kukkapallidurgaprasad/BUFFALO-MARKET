from pydantic import BaseModel

class BuffaloCreate(BaseModel):
    breed: str
    age: int
    milk_per_day: float
    price: float

class BuffaloBuy(BaseModel):
    buffalo_id: int
