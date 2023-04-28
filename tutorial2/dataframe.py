import pandas as pd
df = pd.read_csv("resources/weather_data_tut2.csv")
print(df.head())
print(df.shape)

# slicing (pirnting from row 2 to 5)
print(df[2:5])

#print columns
print(df.columns)

#  Print individual columns
event_column = df.event
day_column = df['day']
print("printing events: ",event_column)
print("---------")
print("printing days",day_column)
print("---------")

# print only some of the columns
print("Printing day and event columns")

print(df[["event", "day"]])

# Dataframe operations
# Find maximum temrature in temprature column
print("Maximum temprature is: ", df['temperature'].max())

# Finding mean
print("Mean temprature is: ", df['temperature'].mean())


# describe (print statastics of data)
print(df.describe())

# Conditional selection
# Select rows with temp greater than 32
print("_____________________________")
print("Printing rows with temprature greateer or equal to 32")
print(df[df.temperature >= 32])
print("-----------------------------------")

print("Selecting rows where temp was MAX")
print(df[df.temperature == df["temperature"].max()])
print("-----------------------------------")

# PRinting some columns and rows with some conditions

print("Printing day and temperature column when th temprature is maximum")
print(df[['day', 'temperature']][df.temperature == df['temperature'].max()])
print("-----------------------------------")

print(df)
# working with index the df assigned automatically
print(df.index)
# Changing the index
print("changing the index")
df.set_index('day', inplace = True)
print(df)
print(df.index)
print("-----------------------------------")

# Now we can use day as index
print("printing a row with any day")
print(df.loc['1/3/2017'])

# Resetting the index to original
print("Resetting the index")
df.reset_index(inplace = True)
print(df)