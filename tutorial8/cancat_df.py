import pandas as pd

# Creating weather dataframe for India
india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
print(india_weather)
print("============================")

# Creating weather dataframe for USA
us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
print(us_weather)
print("==============================")

# Concatinating both the dataframes or Joining both the dataframes into one, as rows

df = pd.concat([india_weather, us_weather])
print(df)



# Fixing the index
print("==============================")
df = pd.concat([india_weather, us_weather], ignore_index= True)
print(df)

# Keys argument, to set key for each dataframe
# Note: Couldnt take ignoreiindex argument. Explained in notes!
print("==============================")
df = pd.concat([india_weather, us_weather], keys = ["india", "us"])
print(df)

# Retreiving data from indian cities
print("==============================")
print(df.loc["india"])

# Concatinating/joining dataframes as columns
print("==============================")
temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])

windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])

df_col = pd.concat([temperature_df, windspeed_df], axis=1)
print(df_col)

# Joining dataframe with a series
print("==============================")
series = pd.Series(["humid", "Dry", "Rain"], name = "event")
df_series = pd.concat([temperature_df, series], axis=1)
print(df_series)


