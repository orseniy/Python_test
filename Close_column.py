import numpy as np
import pandas as pd
import datetime

df = pd.read_csv("../all data/ZUO.csv", sep=',', header=0)
df['Date'] = pd.to_datetime(df['Date'], format="%Y/%m/%d")


df.set_index('Date',inplace=True)
df = df.reindex(pd.date_range(df.index.min(), df.index.max(), freq='D'))
df['3day_before_change'] = df['Close'] / df['Close'].shift(3)
df2 = df.loc[df['Close'].notnull()]
result = df2.sort_index(ascending=False)
print(result)
#result.to_csv("D:/docs/Mykolaiv_test/three_days_column/ZUO_3days_data.csv", index=True)