# Pivot
import pandas as pd
df = pd.read_csv("resources/weather_tut10.csv")
print(df)
print("============================")

# Using pivot
 
df2 = df.pivot(index = "date", columns = "city")
print(df2)
print("============================")


# Pivot Table
df3 = pd.read_csv("resources/weather2_tut10.csv")
print(df3)
print("============================")

# Dealing with multiple values of new york temprature inthe df3
df4 = df3.pivot_table(index="city", columns="date",margins = True, aggfunc = "mean")
print(df4)
print("============================")

# Grouper inn pivot table
df5 = pd.read_csv("resources/weather3_tut10.csv")
print(df5)
print("============================")

# Finding out temprature in a month of may and december
df5["date"] = pd.to_datetime(df5["date"])
df5 = df5.pivot_table(index = pd.Grouper(freq = "M", key = "date"), columns = "city")
print(df5)
