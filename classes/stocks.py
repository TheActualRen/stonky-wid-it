import pandas as pd
import yfinance as yf


class Stock:
    def __init__(self, ticker_symbol: str, from_date: str, to_date: str):
        self.ticker_symbol = ticker_symbol
        self.from_date = from_date
        self.to_date = to_date

        self.ticker: yf.Ticker = yf.Ticker(ticker_symbol)
        self.stock_data: pd.DataFrame = self.ticker.history(
            start=from_date, end=to_date
        )

        self.opens: list[float] = self.stock_data["Open"].tolist()
        self.highs: list[float] = self.stock_data["High"].tolist()
        self.lows: list[float] = self.stock_data["Low"].tolist()
        self.closes: list[float] = self.stock_data["Close"].tolist()

        self.max_y_val = max(self.highs)
        self.min_y_val = min(self.lows)

        self.dates: list[pd.Timestamp] = self.stock_data.index.tolist()
