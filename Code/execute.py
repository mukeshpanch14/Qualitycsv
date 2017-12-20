import ReadModule as RM
#import pandas as pd
#import csv

a = RM.ReadModule('file.csv',1,0,',','\'')
header = a.header_func()
df = a.read_file()
print(type(df[3][16]))
print('**************************')
df[0]=df[0].astype(int)
df[3]=df[3].astype(int)
a = df.groupby([2])[3].count()
print(a)