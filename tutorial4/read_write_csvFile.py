import pandas as pd
df_stocks = pd.read_csv("resources/stock_data.csv")
print(df_stocks)
print("Here we can see a header 'Stocks data' is creating unnecessary drama, so we skip it using the skiprow")

print("_____________________________")
# will use skiprows = 1 to remove the header 
df_stocks = pd.read_csv("resources/stock_data.csv", skiprows=1)
print(df_stocks)

print("_____________________________")
# Here we did the same thing about removing the unnecessary header using the header =1, means the 1st row is the header
df_stocks = pd.read_csv("resources/stock_data.csv", header = 1)
print(df_stocks)

print("_____________________________")
print("what if there is no header?")
df_stocks_without_header = pd.read_csv("resources/stock_data_without_header.csv")
print(df_stocks_without_header)
print(" ")
print("lests put header using 'header = None' and 'names = [header names]' argument")

# working with csv file with no header
df_stocks_without_header = pd.read_csv("resources/stock_data_without_header.csv", header = None, names = ["ticker", "eps", "revenue", "price", "people"])
print(df_stocks_without_header)

print("_____________________________")
# to read n number of rows
print("We use 'nrows = n' to read n number of rows")
df_stocks = pd.read_csv("resources/stock_data.csv", nrows = 3)
print(df_stocks)

print("_____________________________")
# Changing different missing values to NaN
df_stocks = pd.read_csv("resources/stock_data.csv")
print("replacing missing values using 'na_values = [<whatever value you want to turn to NaN>]' argument")
df_stocks = pd.read_csv("resources/stock_data.csv", na_values = ["not available", "n.a."])
print(df_stocks)


print("_____________________________")
# Working with -1 value of revenue, we could not change -1 from revenue dirctly as it would have changed eps value as we  so we used a dictionary
df_stocks = pd.read_csv("resources/stock_data.csv", na_values ={
    'eps' : ["not available", "n.a."],
    'revenue' : ["not available", "n.a.", -1],
    'people' : ["not available", "n.a."]
})
print(df_stocks)
 

# Writing to csv
print("________________________________")
print("We are writing our df_stock csv to a new csv")
df_stocks.to_csv("new_stock.csv", index =False)

# Writing n number of columns only
df_stocks.to_csv("ncolumns_new_stock.csv", columns = ["tickers", "eps"], index = False)
