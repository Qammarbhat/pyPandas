import pandas as pd

# Creating dataframe 1
df1 = pd.DataFrame({
    "city" : ["newyork", "chicago", "orlando"],
    "temprature" : [21, 14, 35]
})
print(df1)
print("=====================")

# Creating dataframe 2
df2 = pd.DataFrame({
    "city" : ["chicago", "newyork", "orlando"],
    "humidity" : [65, 68, 75]
})
print(df2)
print("=====================")
# Merging dataframe 1 and dataframe 2 in dataframe 3

df3 = pd.merge(df1, df2, on = "city")

print(df3)
print("=====================")

# The how argument
df4 = pd.DataFrame({
    "city" : ["newyork", "chicago", "orlando", "san fransisco"],
    "temprature" : [21, 14, 35, 18]
})
print(df4)
print("=====================")


df5 = pd.DataFrame({
    "city" : ["chicago", "newyork", "orlando", "baltimore"],
    "humidity" : [65, 68, 75, 71]
})
print(df5)
print("=====================")

# Merging dataframe 5 and dataframe 6 in dataframe 3

df6 = pd.merge(df4, df5, on = "city", how="outer")

print(df6)
print("=====================")

# Settting how as left
df6 = pd.merge(df4, df5, on = "city", how="left")

print(df6)
print("=====================")

# Settting how as right
df6 = pd.merge(df4, df5, on = "city", how="right")

print(df6)
print("=====================")

# Using indicator argument
df6 = pd.merge(df4, df5, on = "city", how="outer", indicator=True)

print(df6)
print("=====================")

# Using sufixes argument
df7 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})

df8 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
df9 = pd.merge(df7, df8,on= "city", how="outer")
print(df9)

# it used x and y as suffix, lets cahnge it
df9 = pd.merge(df7, df8,on= "city", how="outer", suffixes=("_first", "_second"))
print(df9)