# Import main and dependant libraries
import yfinance as yf
import pandas as pd
import csv

# CONSTANT POINTER TO SORTED DATA
RKLB_DATA = "rklb_info.csv"

# Initialize ticker/stock
ticker = "RKLB"
stock = yf.Ticker(ticker)

# Fetch information for the chosen stock 
stock_info = stock.info

# Convert the default dictionairy format to a dataframe
# Every dictionairy key will create a new row in the dataframe
stock_info_df = pd.DataFrame.from_dict(stock_info, orient='index', columns=['Value'])
stock_info_df.to_csv(RKLB_DATA)
rklb_info_read = pd.read_csv(RKLB_DATA, index_col=0)

print(rklb_info_read.loc[['displayName', 'symbol', 'industry', 'regularMarketOpen', 'allTimeHigh', 'allTimeLow', 'fiftyDayAverage', 'profitMargins', 'marketCap']])