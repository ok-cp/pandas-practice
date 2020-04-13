import pandas as pd

# Load the CSV files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017 = pd.read_csv("./marathon_2015_2017.csv")

# Import pyplot as a alias 'plt'
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Male', 'Female'
# only "explode" the 2nd slice (i.e. 'Female')
explode = (0, 0.1)  
# Configure figure size
plt.figure(figsize=(7,7))
# Creae pie Chart
plt.pie(marathon_2015_2017['M/F'].value_counts(), explode=explode, labels=labels, shadow=True, autopct='%.1f')
# Generate labels and title
plt.title("Male vs. Female",fontsize=18)
# Show plot
plt.show()
