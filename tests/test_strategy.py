import unittest
import pandas as pd
from app.services.strategy_service import calculate_moving_averages, evaluate_strategy

class TestStrategyFunctions(unittest.TestCase):

    def setUp(self):
        self.price_data = pd.DataFrame({"close": [100, 102, 101, 103, 105, 104, 106, 108, 107, 109]})
        self.short_window = 3
        self.long_window = 5

    def test_calculate_moving_averages(self):
        df = calculate_moving_averages(self.price_data, self.short_window, self.long_window)

        self.assertIn("short_ma", df.columns)
        self.assertIn("long_ma", df.columns)

        expected_short = self.price_data["close"].rolling(self.short_window, min_periods=1).mean().iloc[-1]
        expected_long = self.price_data["close"].rolling(self.long_window, min_periods=1).mean().iloc[-1]

        self.assertAlmostEqual(df["short_ma"].iloc[-1], expected_short, places=2)
        self.assertAlmostEqual(df["long_ma"].iloc[-1], expected_long, places=2)

    def test_moving_averages_with_small_dataset(self):
        small_data = pd.DataFrame({"close": [100, 101]})
        df = calculate_moving_averages(small_data, self.short_window, self.long_window)

        self.assertIn("short_ma", df.columns)
        self.assertIn("long_ma", df.columns)

        expected_short = small_data["close"].rolling(self.short_window, min_periods=1).mean().iloc[-1]
        expected_long = small_data["close"].rolling(self.long_window, min_periods=1).mean().iloc[-1]

        self.assertAlmostEqual(df["short_ma"].iloc[-1], expected_short, places=2)
        self.assertAlmostEqual(df["long_ma"].iloc[-1], expected_long, places=2)

    def test_evaluate_strategy_output(self):
        df = calculate_moving_averages(self.price_data, self.short_window, self.long_window)
        result = evaluate_strategy(df)

        expected_keys = {"strategy_total_return (%)", "number_of_trades", "final_trade_signal"}
        self.assertTrue(expected_keys.issubset(result.keys()))

        self.assertIsInstance(result["strategy_total_return (%)"], float)
        self.assertIsInstance(result["number_of_trades"], int)
        self.assertIsInstance(result["final_trade_signal"], str)

if __name__ == "__main__":
    unittest.main()
