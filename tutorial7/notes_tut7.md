# Group By, (Split and Combine)

This code reads a weather data CSV file into a pandas DataFrame and then performs some basic analysis on the data, grouped by cities. The code also generates a plot to visualize the data.

## Importing Libraries

The first few lines of the code import the necessary libraries: pandas for data manipulation, and matplotlib and matplotlib.pyplot for data visualization.

## Reading CSV File

The read_csv() function from pandas is used to read the weather data CSV file into a DataFrame named df. The file is assumed to be located in the 
"resources" folder.

## Grouping Data by Cities

The next step is to group the data in the DataFrame df by the values in the "city" column using the groupby() function. The resulting DataFrameGroupBy object is stored in the variable group_df.

## Accessing Grouped Data

The code then loops through each group in group_df to print the name of the city and the corresponding DataFrame.

## Getting Info of a Particular Group

The code then uses the get_group() function to extract information for a particular group (in this case, the group for the city of Mumbai). The resulting DataFrame is printed.

## Getting Maximum Temperature from Each City

The max() function is used to calculate the maximum value for each column of each group in group_df. The resulting DataFrame is printed.

## Finding Average of Each Column of a Group

The mean() function is used to calculate the average value for each column of each group in group_df. The resulting DataFrame is printed.

## Plotting Data

Finally, the code generates a plot to visualize the data in group_df using the plot() function. The resulting plot is displayed using plt.show().
Functions Used in This Code

    `pd.read_csv()`: reads a CSV file into a pandas DataFrame
    `df.groupby()`: groups the data in a DataFrame by the values in a specified column
    `group_df.get_group()`: extracts information for a particular group from a DataFrameGroupBy object
    `group_df.max()`: calculates the maximum value for each column of each group in a DataFrameGroupBy object
    `group_df.mean()`: calculates the average value for each column of each group in a DataFrameGroupBy object
    `group_df.plot()`: generates a plot of the data in a DataFrameGroupBy object using matplotlib