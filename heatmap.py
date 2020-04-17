# Import pandas as a alias 'pd'
import pandas as pd

# Load the CSV files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017 = pd.read_csv("./marathon_2015_2017.csv")

# Import pyplot as a alias 'plt'
import matplotlib.pyplot as plt
# Import seaborn as a alias 'sns'
import seaborn as sns
sns.set()
# Creatr marathon_2015_2017_under60 dataframe under age 60
# isin()
marathon_2015_2017_under60 = marathon_2015_2017[marathon_2015_2017.Age.isin(range(0,60))]

# Counting by age, Male and Female 
# group by Age, Colum 'M/F' 
# value_counts - groupby count
# unstack - 행과 열을 위치를 바꿈
# fillna - value가 null 인 경우, 0으로 바꿈
marathon = marathon_2015_2017_under60.groupby('Age')['M/F'].value_counts().unstack().fillna(0)
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(10, 20))
# fmt - format
# annot - annotate
sns.heatmap(marathon, annot=True, fmt="d", linewidths=.5, ax=ax)
# blue color
#sns.heatmap(marathon, annot=True, fmt="d", linewidths=.5, ax=ax, cmap="YlGnBu")