from fastapi import APIRouter, Depends
from ..models.database import get_db, engine
from sqlalchemy.orm import Session
from ..data_fetch import fetch_data
from ..models.stock_model import Stock
from app.schemas.stock_schema import StockDataSchema

router = APIRouter(
    tags=['Get Data From SpreadSheet']
)

@router.post("/DataFetch")
def fetch_and_store(db: Session = Depends(get_db)):
    df = fetch_data()

    try:
        for _, row in df.iterrows():
            stock_entry = Stock(
                datetime=row['datetime'],
                close=row['close'],
                high=row['high'],
                low=row['low'],
                open=row['open'],
                volume=int(row['volume']),
            )
            db.add(stock_entry)
        db.commit
        return {"message": "Data inserted successfully!"}
    except Exception as e:
        db.rollback()
        return{"error" : str(e)}


