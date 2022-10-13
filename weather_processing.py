"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries
import pandas as pd
import numpy as np

# TODO Import the dataset 

path = r'./data/weather_dataset.data'
# reading from the file
data=pd.read_csv(path, sep='\s+')
data.head()

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data["data"] = pd.to_datetime((data.Yr*10000+data.Mo*100+data.Dy).apply(str),format='%Y%m%d')

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
# when number is 4,12 except 4.12
for columns in data.columns:
    data[columns] = data[columns].astype(str).str.replace(',', '.')
#change datatype to float32
for columns in data.columns:
    data[columns]=pd.to_numeric(data[columns], errors='coerce', downcast='float')
pd.set_option('display.float_format', lambda x: '%.2f' % x)
#drop unnormal values
data.drop(data.loc[(data['loc9'] >= 50) | (data['loc9'] <= 0)].index, inplace=True)
data.drop(data.loc[(data['loc11'] >= 50) | (data['loc11'] <= 0)].index, inplace=True)
# TODO Write a function in order to fix date (this relate only to the year info) and apply it
def fix_year(x):
    x = x + 1900
    return x

data['Yr'] = data['Yr'].apply(fix_year)
# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
# transform data it to date type datetime64
data["data"] = pd.to_datetime(data["data"])
data = data.drop(columns=['Yr', 'Mo', 'Dy'])
# set data as the index
data = data.set_index('data')

data.head()
# data.info()

# TODO Compute how many values are missing for each location over the entire record
data.isnull().sum()

# TODO Compute how many non-missing values there are in total
data.notnull().sum().sum()

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
windspeeds = data.sum().sum() / data.notna().sum().sum()
windspeeds

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
loc_stats = pd.DataFrame()
loc_stats = data.describe()
#one of all options
loc_stats = loc_stats.drop(index=['count', '25%', '50%', '75%'])


# TODO Find the average windspeed in January for each location
january = data[pd.DatetimeIndex(data.index).month==1].reset_index(drop=True).mean()
#dictionary
dica = dict(january)
dica
#dataframe
january_df = pd.DataFrame(january, columns=['mean'])
january_df

# TODO Downsample the record to a yearly frequency for each location
year_freq = data.resample('Y').mean()
year_freq

# TODO Downsample the record to a monthly frequency for each location
month_freq = data.resample('M').mean()
month_freq

# TODO Downsample the record to a weekly frequency for each location
week_freq = data.resample('W').mean()
week_freq

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
weekly = data.resample('W').agg(['min','max','mean','std'])

weekly_df = weekly.loc['1961-01-02':, :][:21]
weekly_df
