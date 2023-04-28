import pandas as pd
df = pd.read_csv("/home/batm/Projects/pyPanda/tutorial2/weather_data.csv")
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
