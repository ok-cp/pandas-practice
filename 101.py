# Import pandas as a alias 'pd'
import pandas  as pd

# Load the CSV file "marathon_results_2017.csv" under "data" folder
marathon_2017 = pd.read_csv("./marathon_results_2017.csv")

# Display the first five initial rows using the .head() method
print(marathon_2017.head())

# Display data frame structure using the .info() method
print(marathon_2017.info())


#Checking the null values in the data fields
marathon_2017.isnull().sum(axis=0)

#Show columns of the data frame
marathon_2017.columns

#Drop some columns with null values
marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'], axis='columns')

# Display the first five initial rows using the .head() method
print(marathon_2017_clean.head())


# Select runner who's age is more than 60
marathon_2017_clean['Senior'] = marathon_2017_clean.Age > 60

# Select runners from Kennay by conditional expression
marathon_2017_clean['Year'] = '2017'

# Select the column by dot notation
names = marathon_2017_clean.Name

# Display names
print(names)

# Select the column by brackets notation
official_time = marathon_2017_clean['Official Time']

# Display Official Time
print(official_time)


##################

# 1. User defined Function
# Define function name to_seconds
# split(): 구분자를 기준으로 n개로 나눈다, expand=True이면 여러 컬럼, False이면 1개 컬럼에 리스트
def to_seconds(record):
 hms = record.str.split(':', n = 2, expand = True)
 return hms[0].astype(int) * 3600  + hms[1].astype(int) * 60 + hms[2].astype(int)

# Call user defined function to_seconds
marathon_2017['Official Time Sec'] = to_seconds(marathon_2017['Official Time'])

# Display updated data frame with .head() method
print(marathon_2017.head())


# 2. Pre defined Function
# Import Numpy Library and call it as np
import numpy as np

# Convert using pandas to_timedelta method
marathon_2017['Official Time Sec'] = pd.to_timedelta(marathon_2017['Official Time'])

# Convert time to seconds value using astype method
marathon_2017['Official Time New Sec'] = marathon_2017['Official Time Sec'].astype('m8[s]').astype(np.int64)

# Display updated data frame with .head() method
print(marathon_2017.head())

####################