import pandas as pd

df = pd.read_csv("titanic.csv")
print(df['Age'].min())

print(df.groupby('Age').count())
