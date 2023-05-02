import pandas as pd
import numpy as np

df = pd.read_csv("resources/weather_data_tut6.csv")
print(df)

# replacing the -99999 unwanted value
print("________________________________")
print("replacing the unwanted values")
# new_df = df.replace(-99999, np.NaN)

# new_df = df.replace(-88888, np.NaN)

# We can replace multible unwanted values from our df as follows
new_df = df.replace([-99999, -88888], np.NaN)
print(new_df)

# Replace values based on specfic columns
print("==============================")
new_df2 = df.replace({
    'temperature' : [-99999, -88888],
    'windspeed' : [-99999, -88888],
    'event' : '0'
}, np.NaN)
print("Replaced unwanted values based on columns, used dictionary")
print(new_df2)

# Working with new data with "No event as some value of event"
print("============================================")
print("============================================")

df_noEvent = pd.read_csv("resources/weather_data_tut6_noEvent.csv")
print(df_noEvent)
print("=========================")
# Replacing No Event with "Sunny", and -9999 with NaN
new_df_noEvent = df_noEvent.replace({
    -99999 : np.NaN,
    'No Event' : 'Sunny'
})
print(new_df_noEvent)

print("=========================")
# Working with the unwanted units in some columns
print("Working with the units in some columns,using regex to deal with these units")
new_df_noEvent = df_noEvent.replace({
    'temperature' : '[A-Za-z]',
    'windspeed' : '[A-Za-z]',
}, '', regex=True)
print(new_df_noEvent)

# Replacing texts with number
# Create a new dataframe
print("=====================================")
df_score = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})

print(df_score)
print("=====================================")
# lets map these grades like poor good ets with numbers
new_df_score = df_score.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
print(new_df_score)