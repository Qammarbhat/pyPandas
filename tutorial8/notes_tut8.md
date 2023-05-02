# Concatination in Python Pandas

In Pandas, concatenation is the process of combining two or more dataframes or series into a single dataframe or series. The resulting dataframe or series can be concatenated either as rows or as columns.

The `pd.concat()` function in Pandas is used to perform concatenation. It takes a list of dataframes or series to be concatenated as its first argument.

The `axis` parameter is used to specify the axis along which the concatenation is to be performed. An `axis` value of 0 means that the concatenation is performed along the rows (vertically), while an axis value of 1 means that the concatenation is performed along the columns (horizontally).

The `keys` parameter can be used to specify the keys for the resulting dataframe or series. If specified, the resulting dataframe or series will have a hierarchical index with the keys specified.

By default, the indices of the input dataframes or series are retained in the resulting dataframe or series. The `ignore_index` parameter can be set to `True` to ignore the original indices and create a new index for the resulting dataframe or series.

Concatenation is a powerful tool in Pandas as it allows you to combine data from multiple sources and manipulate it in various ways. It is often used in data preprocessing and data cleaning tasks.
## Libraries Imported

pandas: A library used for data manipulation and analysis.

## Creating DataFrames

Two DataFrames are created, one for India and one for the USA, each containing information on the temperature and humidity of different cities.
The DataFrames are created using the pd.DataFrame() function, with a dictionary containing the data.

## Concatenating DataFrames

The two DataFrames are concatenated using the pd.concat() function, with the two DataFrames passed as a list to the function.
By default, the DataFrames are concatenated as rows, but this can be changed using the 'axis' argument, which specifies whether to concatenate columns (axis=1) or rows (axis=0).
The function returns a new DataFrame containing both original DataFrames.

## Fixing Index

When concatenating two DataFrames, the index can become duplicated. This can be fixed using the 'ignore_index' argument of the pd.concat() function, which will reset the index to start from 0.

## Keys Argument

The 'keys' argument of the pd.concat() function is used to create a hierarchical index for the resulting DataFrame. It takes a list of keys that correspond to the order of the DataFrames passed in the concatenation. The resulting DataFrame will have a multi-level index, with each key representing one level.

## Retrieving Data

Using the .loc[] function, data from specific keys of the resulting DataFrame can be retrieved. In this case, data from the "india" key is retrieved.

## Concatenating DataFrames as Columns

DataFrames can also be concatenated as columns using the 'axis' argument, which is set to 1.
    
Two new DataFrames are created, one containing temperature data and the other containing wind speed data.
    
These DataFrames are then concatenated as columns to create a new DataFrame.

## Joining DataFrame with a Series

A Series is a one-dimensional array-like object that can hold any data type, such as integers, strings, or even other objects.
    
In this example, a new Series containing event data is created and joined with the temperature DataFrame.
    
The two are joined as columns using the pd.concat() function, and a new DataFrame is returned.

## Functions Used in the code:

`pd.DataFrame()` - This function is used to create a new DataFrame from a dictionary.
    
`pd.concat()` - This function is used to concatenate two or more dataframes either vertically or horizontally.
    
`print()` - This function is used to print the output to the console.
    
`df.loc[]` - This function is used to retrieve rows from a DataFrame by label.
    
`pd.Series()` - This function is used to create a new series in pandas.
    
`index=[]` - This parameter is used to set the index for the dataframe or series. If not provided, a default numeric index is used.
    
`axis=1` - This parameter is used to concatenate dataframes horizontally (i.e. along columns).
    
`name=` - This parameter is used to set the name of the series.