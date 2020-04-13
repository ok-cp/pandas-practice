# Import pandas as a alias 'pd'
import pandas as pd

# Load the CSV files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017 = pd.read_csv("./data/marathon_2015_2017.csv")

# Import pyplot as a alias 'plt'
import matplotlib.pyplot as plt

# Select runners from Age 18 to 60 by conditional expression
runner_1860 = marathon_2015_2017[marathon_2015_2017.Age.isin(range(18,60))]

# Create runner_1860_counting Dataframe with counting by Age
runner_1860_counting = runner_1860['Age'].value_counts()

# Create new dataframe
runner_age = pd.DataFrame({
    'Age' : runner_1860_counting.index,
    'Count' : runner_1860_counting
})

runner_age_sort = runner_age.sort_values(by=['Age'])

# Store index of runner_1860_counting into x
# sort age
x = runner_age_sort.index
# x = runner_1860_counting.index

# Conver x values to String in order to avoid int sorting
x = [str(i) for i in x]

# Store values of runner_1860_counting into y
# sort count
y = runner_age_sort['Count']
# y = runner_1860_counting.values

# Calculate ratio and accumulated ratio
ratio = y / y.sum()
ratio_sum = ratio.cumsum()
y_ratio = [i for i in ratio_sum]

# Configure figure size
fig, barChart = plt.subplots(figsize=(20,10))
# Creae bar Chart
barChart.bar(x, y)
# Creae line Chart
lineChart = barChart.twinx()
lineChart.plot(x, ratio_sum, '-ro', alpha=0.5)

# Creae right side labels
ranges = lineChart.get_yticks()
lineChart.set_yticklabels(['{:,.1%}'.format(x) for x in ranges])


# Creae annotations on line chart
ratio_sum_percentages = ['{0:.0%}'.format(x) for x in ratio_sum]

for i, txt in enumerate(ratio_sum_percentages):
    lineChart.annotate(txt, (x[i], y_ratio[i]), fontsize=14)    
    # lineChart.annotate(txt, (x[i], ratio_sum[i]), fontsize=14)    

# Generate labels and title
barChart.set_xlabel('Age', fontdict= {'size':16})
barChart.set_ylabel('Number of runner', fontdict= {'size':16})
plt.title('Pareto Chart - Number of runner by Age', fontsize=18)
# Show plot
plt.show()
