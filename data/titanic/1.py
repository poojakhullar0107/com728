#task 1
#coding using panda for number of records in csv file

import pandas as pd
print("loading Data....")
df=pd.read_csv("titanic.csv")
print(df.shape[0])

#task 3
#coding using paanda for print name from csv file

import pandas as pd

df = pd.read_csv("titanic.csv", usecols=['Name'])
print(df)
