import numpy as np
import pandas as pd

# df = pd.read_csv('salaries.csv')

# print(df['Salary'].mean())

# print(df[df['Age']>30])
#   Equivalent to:
#   ser_of_bool = df['Age'] > 30
#   print(df[ser_of_bool])

# print(df['Age'].unique())
# print(df['Age'].nunique())
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df.index)

mat = np.arange(0,10).reshape(5,2)

df = pd.DataFrame(data = mat, columns=['A','B'], index=['NY','London', 'Paris', 'Tokio', 'Mumbai'])
print(df)
