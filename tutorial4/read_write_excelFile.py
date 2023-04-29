import pandas as pd

# Readng excel file
df_stocks = pd.read_excel("resources/stock_data.xlsx")
print(df_stocks)

# Writing to excel file
df_stocks.to_excel("new.xlsx", sheet_name = "stocks")

print("__________________________________________")
# Writing two df to different sheet of excel
df_stocks1 = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks1.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
