import ReadModule as RM
#import pandas as pd
#import csv

#a = RM.ReadModule('file.csv',1,0,',','\'')
a = RM.ReadModule('file.csv',1,0,',','\'')
header = a.header_func()
df = a.read_file(['Emp_Name','City'])
print('**************************')
print(df)