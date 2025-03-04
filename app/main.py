from fastapi import FastAPI
from .routes import fetch_route, Stock_route, strategy_route
from .models.database import engine
from .models.stock_model import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(fetch_route.router)
app.include_router(Stock_route.router)
app.include_router(strategy_route.router)