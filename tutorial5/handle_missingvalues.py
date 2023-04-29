import pandas as pd
df_weather = pd.read_csv("resources/weather_data_tut5.csv")
print(df_weather)

# converting datatype, type(df.day[0]) from string to date
print(type(df_weather.day[0]))
print("As you can see day column is of type str")

print("_______________________________")
# use parse_dates argument
df_weather = pd.read_csv("resources/weather_data_tut5.csv", parse_dates = ["day"])
print(df_weather)

# Usinf day colums as index
print("_______________________________")
print("Will use day column as index")
df_weather.set_index("day", inplace = True)
print(df_weather)


# Using filll na to fill NaN values
print("_______________________________")
new_df_weather = df_weather.fillna(0)
print(new_df_weather)

# it doesnt make any sense to have 0 in event column so lets fix it 
print("_______________________________")
print("it doesnt make any sense to have 0 in event column so lets fix it ")
new_df_weather = df_weather.fillna({
    'temperature': 0,
    'windspeed' : 0,
    'event' : 'no event'

})
print(new_df_weather)

# it still doesnt make sense to have 0 temperature so we can use the previous value as the new NaN value
# USing df.fillna(method =  ffill), ffill mean forward valuie
# Can also use fillna(method = bfill), to put the value of next value

print("________________________________________________")
print("it still doesnt make sense to have 0 temperature so we can use the previous value as the new NaN value")
new_df_weather = df_weather.fillna(method = "ffill")
print(new_df_weather)


print("______________________________________________________")
# Using interpolate
# We can make it better by using interpolte to fill tha na values by better values as shown below
#  by default it used linear interpolation so it cam eup with the middle value
new_df_weather = df_weather.interpolate()
print(new_df_weather)

# lets use method =  time
print("______________________________________________________")
new_df_weather = df_weather.interpolate(method = "time")
print(new_df_weather)
# Now it make sense as 4th jan is close to 5th thus the temp value should be close to 28 not in the middle of 32 and 28


# Using dropna to drop rows with missing value
print("______________________________________________________")
df_weather_dropNa = df_weather.dropna()
print(df_weather_dropNa)

# it dropped all rows with even just 1 NaN value
# lets drop row if it has all the mssing values
print("______________________________________________________")
df_weather_dropNa = df_weather.dropna(how = "all")
print(df_weather_dropNa)

# if I have atleast 1 NaN value, keep the row ( I need 1 valid value to keep the row)
print("______________________________________________________")
df_weather_dropNa = df_weather.dropna(thresh= 1)
print(df_weather_dropNa)

# Inserting missing dates
print("______________________________________________________")
dt = pd.date_range("01-01-2017", "01-11-2017")
idx = pd.DatetimeIndex(dt)
df_weather = df_weather.reindex(idx)
print(df_weather)
