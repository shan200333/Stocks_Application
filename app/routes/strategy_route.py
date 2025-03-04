from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any, List
from ..models.database import SessionLocal, get_db
from ..models.stock_model import Stock
from ..services.strategy_service import process_stock_data 

router = APIRouter(
    tags=['Stock Performance']
)

@router.get("/strategy/performance", response_model=Dict[str, Any])
def get_strategy_performance(db: Session = Depends(get_db)):
    stock_data: List[Stock] = db.query(Stock).order_by(Stock.Created_At).all()
    
    if not stock_data:
        raise HTTPException(status_code=404, detail="No stock data available.")

    return process_stock_data(stock_data)
