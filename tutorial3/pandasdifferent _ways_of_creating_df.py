import pandas as pd
import os
# print(os.getcwd())

# Reading the csv file
print("Reading the csv file using pd.read_csv")
df = pd.read_csv("resources/weather_data_tut3.csv")
print(df.head())

print("_______________________________")
# Reading the excel file
print("Reading the excel file")
df_excel = pd.read_excel("resources/weather_data.xlsx")
print(df_excel)


# creating dataframe using python dictionary
print("_______________________________")
print("Creating dataframe using py dictionary")

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}

df_dict = pd.DataFrame(weather_data)
print(df_dict)

# Creating datafare using tuple list
print("_______________________________")
print("Creating dataframe using a tuplelist")
weather_data_tuple = weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df_tuple = pd.DataFrame(weather_data_tuple, columns= ['day', 'temperature', 'windspeed', 'event'])
print(df_tuple)

# Creating data frame using list of dictionaries

print("_______________________________")
print("creating data frame using the list of dictionaries")

weather_list_dict = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    
]

df_list_dict = pd.DataFrame(weather_list_dict)
print(df_list_dict)