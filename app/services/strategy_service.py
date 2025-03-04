import pandas as pd
import numpy as np
from typing import Dict, Any, List

def calculate_moving_averages(df: pd.DataFrame, short_window: int = 5, long_window: int = 20) -> pd.DataFrame:
    df["short_ma"] = df["close"].rolling(window=short_window, min_periods=1).mean()
    df["long_ma"] = df["close"].rolling(window=long_window, min_periods=1).mean()

    df["signal"] = np.where(df["short_ma"] > df["long_ma"], 1, -1)  

    return df

def evaluate_strategy(df: pd.DataFrame) -> Dict[str, Any]:
    df["returns"] = df["close"].pct_change()
    df["strategy_returns"] = df["signal"].shift(1) * df["returns"]

    strategy_performance = {
        "strategy_total_return (%)": round(float(df["strategy_returns"].sum() * 100), 2),
        "number_of_trades": int(df["signal"].abs().sum()),
        "final_trade_signal": "Buy" if df["signal"].iloc[-1] == 1 else "Sell" if df["signal"].iloc[-1] == -1 else "Hold"
    }
    
    return strategy_performance

def process_stock_data(stock_data: List) -> Dict[str, Any]:
    df = pd.DataFrame(
        [{"datetime": record.Created_At, "close": float(record.close)} for record in stock_data]
    )

    df = calculate_moving_averages(df)
    return evaluate_strategy(df)
