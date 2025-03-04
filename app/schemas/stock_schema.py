from pydantic import BaseModel, Field
from datetime import datetime

class StockDataSchema(BaseModel):
    Created_At: datetime | None = None
    open : float
    high : float
    low : float
    close : float
    volume : int

class Post(StockDataSchema):
    id: int

class CreateStock(BaseModel):
    Created_At : datetime = Field(default_factory=datetime.utcnow) 
    open : float
    high : float
    low : float
    close : float
    volume : int