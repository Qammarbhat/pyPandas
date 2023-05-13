# Crosstb in Pnadas
The `pd.crosstab()` function in Pandas is used to create cross-tabulations (frequency tables) of one or more variables in a dataframe. It counts the number of times each combination of values in the specified columns occurs and creates a new dataframe with the counts. The function takes one or more columns of the dataframe as arguments, and can also take the "margins" argument to add total counts to the crosstab. Additionally, it can take multiple columns as arguments to create a crosstab of more than two variables.

The `pd.crosstab()` function in Pandas is a very powerful tool for creating frequency tables of one or more variables in a dataframe. It can be used to quickly and easily summarize the data and gain insights into patterns and relationships between variables.

The function takes one or more columns of the dataframe as arguments and creates a crosstab of the variables specified. It counts the number of times each combination of values in the columns occurs and creates a new dataframe with the counts.

For example, if we have a dataframe of customer purchases with columns for "Product", "Gender", and "Age Group", we can create a crosstab of the number of purchases of each product by gender and age group by using the following code:

`pd.crosstab(df.Product, [df.Gender, df.Age_Group])`

This will create a crosstab that shows the number of purchases of each product by gender and age group, with each combination of values represented in a cell of the table.

The `pd.crosstab()` function can also take the "margins" argument to add total counts to the crosstab. When "margins" is set to "True", it creates a row and column that show the total count of each category in the crosstab.

Additionally, it can take multiple columns as arguments to create a crosstab of more than two variables. This can be useful for exploring the relationships between multiple variables and identifying patterns and trends in the data.

Overall, the `pd.crosstab()` function is a powerful tool for exploring and summarizing data in Pandas, and is widely used in data analysis and machine learning applications.

# Code Summary
```
import pandas as pd
df = pd.read_excel("resources/survey_tut13.xls")
print(df)
print("========================================")

# Using crosstable
new_df = pd.crosstab(df.Nationality, df.Handedness)
print(new_df)

print("========================================")
# The margin argument

new_df = pd.crosstab(df.Sex, df.Handedness, margins = True)
print(new_df)
print("========================================")

# Using more than two variable
new_df = pd.crosstab(df.Sex, [df.Handedness, df.Nationality], margins = True)
print(new_df)
```

# Using crosstable
` new_df = pd.crosstab(df.Nationality, df.Handedness)`
print(new_df)

print("========================================")
# The margin argument

new_df = pd.crosstab(df.Sex, df.Handedness, margins = True)
print(new_df)
print("========================================")

# Using more than two variable
new_df = pd.crosstab(df.Sex, [df.Handedness, df.Nationality], margins = True)
print(new_df)

This code imports the Pandas library and reads an Excel file called "survey_tut13.xls" into a Pandas dataframe named "df". It then prints the dataframe to the console and separates the output from the next section with a line of equal signs.

The code then uses the `pd.crosstab()` function to create a new dataframe named "new_df" that shows the frequency distribution of handedness and nationality. The crosstab function counts the number of times each combination of values in the two columns occurs, and creates a new dataframe with the counts.

The code then prints the new dataframe to the console and separates the output from the next section with a line of equal signs.

Next, the code creates another crosstab of handedness and sex, with the "margins" argument set to "True". The margins argument creates a row and column that show the total count of each category in the crosstab.

The code prints this new dataframe to the console and separates the output from the next section with a line of equal signs.

Finally, the code creates another crosstab of handedness, nationality, and sex, with the margins argument set to True. This creates a more complex crosstab with three variables. The resulting dataframe is printed to the console.

Overall, this code demonstrates how to use the `pd.crosstab()` function in Pandas to create frequency tables for one or more variables in a dataframe. It also shows how to use the "margins" argument to add total counts to the crosstab.


# Functions used in this code
1. `pd.read_excel()`
`pd.read_excel("resources/survey_tut13.xls")`

This function is used to read an Excel file into a Pandas dataframe. It takes the file path as an argument. In this case, it reads the file "survey_tut13.xls" from the "resources" folder.

2. `pd.crosstab()`
`pd.crosstab(df.Nationality, df.Handedness)`
This function creates a cross-tabulation (or frequency table) of two or more variables in a Pandas dataframe. It takes one or more columns of the dataframe as arguments. In this case, it creates a crosstab of the "Nationality" and "Handedness" columns in the dataframe "df".

` pd.crosstab(df.Sex, df.Handedness, margins=True)`
The function can also take the "margins" argument to add total counts to the crosstab. When "margins" is set to "True", it creates a row and column that show the total count of each category in the crosstab.

`pd.crosstab(df.Sex, [df.Handedness, df.Nationality], margins=True)`
Additionally, `pd.crosstab()` can take multiple columns as arguments to create a crosstab of more than two variables. In this case, it creates a crosstab of "Sex", "Handedness", and "Nationality" columns in the dataframe "df".





