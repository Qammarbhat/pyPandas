import pandas as pd
import os
print(os.getcwd())
df = pd.read_csv("resources/weather_data_tut3.csv")
print(df.head())