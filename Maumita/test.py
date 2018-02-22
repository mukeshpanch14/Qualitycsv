import pandas as pd

df=pd.read_csv("file.csv",quotechar='\'')
n=print(df["Emp_Id"])
x=pd.isnull(n)
print(x)
