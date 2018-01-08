import ReadModule_new as RM
#import pandas as pd
#import csv

a = RM.ReadModule('file.csv',1,0,',','\'')
header = a.header_func()
df = a.read_file()
print('**************************')
print(df)