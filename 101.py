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
