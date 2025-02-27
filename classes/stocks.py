import yfinance as yf
import pandas as pd


class Stock:
    def __init__(self, ticker_symbol: str, from_date: str, to_date: str):
        self.ticker_symbol = ticker_symbol
        self.from_date = from_date
        self.to_date = to_date

        self.ticker: yf.Ticker = yf.Ticker(ticker_symbol)
        self.stock_data: pd.DataFrame = self.ticker.history(start=from_date, end=to_date)
