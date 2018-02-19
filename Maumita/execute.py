import ReadModule as RM
import NullCheck as NC
import DuplicateCheck as D
#import pandas as pd
#import csv

#a = RM.ReadModule('file.csv',1,0,',','\'')
a = RM.ReadModule('file.csv',1,0,',','\'')
#header = a.header_func()
df = a.read_file(['Emp_Id','Emp_Name','City','DOB'])
#print('**************************')
#print(df)
#print('**************************')
#rule_nullcheck = NC.NullCheck(df,['Emp_Name'])
#rule_nullcheck.checkNull()
dup=D.Duplicate(df,col_list=['Emp_Name','City'])
dup.duplicate()