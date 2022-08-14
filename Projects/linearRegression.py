import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
#print(df.head())

df = [["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume",]]
df["HL percent"] = (df["Adj. High"] - df["Adj. Close"]) / df["Adj. Close"] * 100.0

df["Percent Change"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"] * 100.0

print(df[["Adj. Close", "HL percent", "Percent Change", "Adj. Volume"]])