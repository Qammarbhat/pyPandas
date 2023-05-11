# melt

import pandas as pd
df = pd.read_csv("resources/weather_tut11.csv")
print(df)
print("================================")

# Using melt to reshape our df
df1 = pd.melt(df, id_vars=["day"])
print(df1)
print("==================================")

# filtering out the data, where city is chicago
print(df1[df1.variable == "chicago"])
print("==============================")

# filtering out the data, where value/temprature is 22
print(df1[df1.value == 22])
print("==============================")

# filtering out the data, where day is monday
print(df1[df1["day"]== "Monday"])
print("==============================")

# Changing the names of columns (variable --> city, value --> temprature)
df1 = pd.melt(df, id_vars=["day"], var_name="city", value_name="temprature")
print(df1)
