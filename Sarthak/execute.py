import ReadModule as RM
import NullCheck as NC
import WriteModule as WM
#import pandas as pd
#import csv

#a = RM.ReadModule('file.csv',1,0,',','\'')
a = RM.ReadModule('file.csv',1,0,',','\'')
header = a.header_func()
df = a.read_file(['Emp_Name','City'])
print('**************************')
print(df)
print('**************************')
#rule_nullcheck = NC.NullCheck(df,['Emp_Name'])
#rule_nullcheck.checkNull()
file = 'write_out.csv'
header = [['Rule_ID','Status']]
data = [['1','Success'],['2','Failure']]
write = WM.WriteModule(file,header,data)
write.write()