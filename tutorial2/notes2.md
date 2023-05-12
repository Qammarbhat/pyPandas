# Dataframe Basics

# Pandas Dataframe Operations

## Reading Data
- Reading a CSV file using pandas' `read_csv()` function
- The resulting DataFrame is stored in the variable `df`

## Basic Operations
### Slicing
- Slicing and printing rows 2 to 5 of the DataFrame using `df[2:5]`

### Printing Columns
- Printing all columns in the DataFrame using `df.columns`
- Printing individual columns using `df.<column_name>` or `df['<column_name>']`

### Selecting Specific Columns
- Printing specific columns using `df[['<column_name_1>', '<column_name_2>']]`

## Dataframe Operations
### Basic Statistics
- Finding the maximum temperature in the temperature column using `df['temperature'].max()`
- Finding the mean temperature in the temperature column using `df['temperature'].mean()`

### Describing Data
- Printing statistics of all columns using `df.describe()`

### Conditional Selection
- Selecting rows with temperature greater than or equal to 32 using `df[df.temperature >= 32]`
- Selecting rows where temperature is maximum using `df[df.temperature == df["temperature"].max()]`
- Printing day and temperature column when the temperature is maximum using `df[['day', 'temperature']][df.temperature == df['temperature'].max()]`

## Working with Index
### Assigning Index
- Printing the current index of the DataFrame using `df.index`
- Assigning a new index using `df.set_index('<index_column_name>', inplace=True)`

### Using Index
- Printing a row with a specific day using `df.loc['<day_value>']`

### Resetting Index
- Resetting the index to the original integer index using `df.reset_index(inplace=True)`

