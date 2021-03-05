#coding using panda for number of records in csv file

import pandas as pd
print("loading Data....")
df=pd.read_csv("titanic.csv")
print(df.shape[0])




