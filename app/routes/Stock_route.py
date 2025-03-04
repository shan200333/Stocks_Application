from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import stock_model
from ..models.database import SessionLocal, get_db
from ..models.stock_model import Stock
from ..schemas.stock_schema import StockDataSchema, CreateStock
from ..schemas import stock_schema

router = APIRouter(
    tags=['Stock Operations']
)

@router.get("/Stocks", response_model=list[StockDataSchema])
def get_all_data(db: Session = Depends(get_db)):
    records = db.query(Stock).all()

    if not records:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail=f"No records were found")
    return records

@router.post("/Stocks", status_code=status.HTTP_201_CREATED, response_model=stock_schema.Post)
def create_stocks(post: CreateStock, db: Session = Depends(get_db)):
    stock_data = post.dict(exclude_unset=True)
    new_stock = stock_model.Stock( **post.dict())
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock

