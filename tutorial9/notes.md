# Pandas DataFrame Merging

In this code, we are using the pandas library to create and merge multiple dataframes.

## Creating DataFrames

Two DataFrames, df1 and df2, are created using the pandas DataFrame function. The first DataFrame, df1, contains city and temperature information. The second DataFrame, df2, contains city and humidity information.
Merging DataFrames

We merge df1 and df2 into a new DataFrame, df3, using the merge() function. We specify that we want to merge on the "city" column using the "on" argument.

## Merge Types

We create two more DataFrames, df4 and df5, that have different cities than df1 and df2. We then use the merge() function to merge these DataFrames. We specify the `how` argument to determine the type of merge we want to perform.

1. `outer` : Performs a full outer join, which includes all rows from both DataFrames.
    
`left` : Performs a left outer join, which includes all rows from the left DataFrame and any matching rows from the right DataFrame.
    
`right` : Performs a right outer join, which includes all rows from the right DataFrame and any matching rows from the left DataFrame.

We can also use the "indicator" argument to add a column to the merged DataFrame that indicates the source of each row.

## Suffixes

We create two more DataFrames, df7 and df8, that have different city names than df1, df2, df4, and df5. We then use the merge() function to merge these DataFrames. We specify the `suffixes` argument to add a suffix to any column names that are duplicated across DataFrames.

## Functions Used

Here are the functions used in this code along with their brief definitions:

`pd.DataFrame()`: Creates a new pandas DataFrame.
`pd.merge()` : Merges two or more pandas DataFrames based on specified columns.
`DataFrame.print()` : Prints the DataFrame to the console.
`DataFrame.rename()` : Renames columns of a DataFrame.
`DataFrame.drop()` : Drops specified labels from rows or columns of a DataFrame.