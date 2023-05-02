import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
df = pd.read_csv("resources/weather_by_cities_tut7.csv")
print(df)
print("=======================================")

# Let's group the data by cities
print("Let's group the data by cities")
group_df = df.groupby('city')
print(group_df)

# Accessing the grouped data
print("=======================================")
for city, city_df in group_df:
    print(city)
    print(city_df)

# Getting info of a particular group
print("=======================================")
print(group_df.get_group('mumbai')) 

# Getting maximum tempraturefrom each group/ccity
print("=======================================")
print(group_df.max())

# finding average of each column of a group
print("=======================================")
print(group_df.mean())

# Plotting
# %matplotlib inline
group_df.plot()
plt.show()
