# Import pandas as a alias 'pd'
import pandas as pd

# Load the CSV files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017 = pd.read_csv("./marathon_2015_2017.csv")

# Import pyplot as a alias 'plt'
import matplotlib.pyplot as plt
# Import seaborn as a alias 'sns'
import seaborn as sns

marathon_2015_2017.head()

# Select runners from USA by conditional expression
USA_runner = marathon_2015_2017[marathon_2015_2017.Country == 'USA']

USA_runner.info()

# Configure figure size
plt.figure(figsize=(20,10))
# Number of Runner by State - USA
runner_state = sns.countplot('State',data=USA_runner)
runner_state.set_title('Number of Runner by State - USA', fontsize=18)
runner_state.set_xlabel('State', fontdict= {'size':16})
runner_state.set_ylabel('Number of Runner', fontdict= {'size':16})
plt.show()

plt.figure(figsize=(20,10))
# Number of Runner by State, Gender - USA
runner_state = sns.countplot('State',data=USA_runner, hue='M/F',  palette={'F':'r','M':'b'})
runner_state.set_title('Number of Runner by State, Gender - USA', fontsize=18)
runner_state.set_xlabel('State', fontdict= {'size':16})
runner_state.set_ylabel('Number of Runner', fontdict= {'size':16})
plt.show()

plt.figure(figsize=(20,10))
# Number of Runner by State, year - USA
runner_state = sns.countplot('State',data=USA_runner, hue='Year')
runner_state.set_title('Number of Runner by State, year - USA', fontsize=18)
runner_state.set_xlabel('State', fontdict= {'size':16})
runner_state.set_ylabel('Number of Runner', fontdict= {'size':16})
plt.show()


