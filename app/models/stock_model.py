from sqlalchemy import Column, TIMESTAMP, Integer, DECIMAL, func
from .database import Base

class Stock(Base):
    __tablename__ = "Stocks"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    Created_At = Column(TIMESTAMP, server_default=func.now(), index=True)
    open =  Column(DECIMAL)
    high = Column(DECIMAL)
    low = Column(DECIMAL)
    close = Column(DECIMAL)
    volume = Column(Integer)

