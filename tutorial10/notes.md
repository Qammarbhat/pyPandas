# Pivot and Pivot Table in Pandas

The Pandas library in Python provides two powerful methods for reshaping data: pivot() and pivot_table(). These methods allow you to transform a DataFrame from a long format to a wide format, making it easier to analyze and visualize.

## `pivot()` method

The pivot() method allows you to reshape a DataFrame by converting values from one or more columns into new columns. It takes the following arguments:

`index` : Column to use as the index of the pivoted DataFrame.
    
`columns` : Column to use as the columns of the pivoted DataFrame.

`values` : Column to use as the values of the pivoted DataFrame.

```
import pandas as pd

# read the CSV file into a DataFrame
df = pd.read_csv("resources/weather_tut10.csv")
print(df)
print("============================")

# Using pivot
df2 = df.pivot(index="date", columns="city")
print(df2)
print("============================")
```
In this code, we read a CSV file into a DataFrame and then use the `pivot()` method to pivot the DataFrame. We set the `date` column as the index and the `city` column as the columns of the pivoted DataFrame.

## `pivot_table()` method

The `pivot_table()` method is similar to `pivot()`, but it allows you to aggregate values based on one or more columns. It takes the following arguments:

`values` : Column to use as the values of the pivoted DataFrame.
    
`index` : Column to use as the index of the pivoted DataFrame.
    
`columns`: Column to use as the columns of the pivoted DataFrame.
    
`aggfunc` : Function to use for aggregating the values.
    
`margins` : Adds row/column subtotals and grand total.

```
# read the CSV file into a DataFrame
df3 = pd.read_csv("resources/weather2_tut10.csv")
print(df3)
print("============================")

# Dealing with multiple values of new york temperature in the df3
df4 = df3.pivot_table(index="city", columns="date", margins=True, aggfunc="mean")
print(df4)
print("============================")
```
In this code, we read a CSV file into a DataFrame and then use the `pivot_table()` method to pivot the DataFrame. We set the `city` column as the index, the `date` column as the columns, and the `mean` function as the aggregation function to be used. We also set `margins` to `True` to add subtotals and grand total.

## `Grouper()` function

The `Grouper()` function is used to group time series data by a specific frequency. It takes the following arguments:

`freq` : Frequency at which to group the data.
`key` : Column to use as the key for grouping.

```
# read the CSV file into a DataFrame
df5 = pd.read_csv("resources/weather3_tut10.csv")
print(df5)
print("============================")

# Finding out temperature in a month of May and December
df5["date"] = pd.to_datetime(df5["date"])
df5 = df5.pivot_table(index=pd.Grouper(freq="M", key="date"), columns="city")
print(df5)
```
In this code, we read a CSV file into a DataFrame and convert the `date `column to a `datetime` object. We then use the `pivot_table()` method to pivot the DataFrame by grouping the data by month using the `Grouper()` function

## Functions used in the code:

`pd.read_csv()` - This function is used to read a CSV file and create a DataFrame object from it.

    
`df.pivot()` - This function is used to create a pivot table from the given DataFrame.

`df.pivot_table()` - This function is used to create a pivot table from the given DataFrame. It allows to use aggregation functions on the values.

`pd.Grouper()` - This function is used to create a time-based grouping object that can be passed to the df.pivot_table() function.

`pd.to_datetime()` - This function is used to convert the date column of the DataFrame into the datetime format.