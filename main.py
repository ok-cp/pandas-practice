import pandas as pd
from collections import OrderedDict

flist =  [
    {'name': 'John', 'age': 25, 'job': 'student'},
    {'name': 'Sam', 'age': 35, 'job': 'staff'}
]

df1 = pd.DataFrame(flist)
df1 = df1[['name', 'job', 'age']]
# df = pd.read_csv('./student.csv')
print(df1.head())

Olist = OrderedDict(
    [
        ('name', ['John', 'Nate']),
        ('age', [25, 30]),
        ('job', ['student', 'staff'])

    ]
)

df2 = pd.DataFrame.from_dict(Olist)

print(df2)