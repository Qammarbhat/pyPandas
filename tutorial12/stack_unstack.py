#Stacking and unstacking

#Stack unstack
import pandas as pd
df = pd.read_excel("resources/stocks_tut12.xlsx", header = [0,1])
print(df)
print("=================================")

# Stacking header 1 (inner most level of headers) into columnss
df1 = df.stack()
print(df1)
print("=========================")

# Stacking first level of header into columns
df2 = df.stack(level=0)
print(df2)
print("======================================")
# using unstack to unstack
df2 = df2.unstack()
print(df2)
