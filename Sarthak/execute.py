import ReadModule as RM
import NullCheck as NC
import WriteModule as WM
import DataTypeCheck as DTC
import pandas as pd
#import csv

#a = RM.ReadModule('file.csv',1,0,',','\'')
a = RM.ReadModule('file.csv',1,0,',','\'')
header = a.getHeader()
df = a.read_file(['Emp_Id','Emp_Name','DOB'])
print('**************************')
#print(df)
print('**************************')
rule_nullcheck = NC.NullCheck(df,['Emp_Name'])
rule_nullcheck.checkNull()
file_name='write_out.csv'
#header_data=[['Rule Id','Run Date','Run Time','Subject Area','Rule Name','Rule Sub Ctgy','Rule Description','Attribute Name','File Name','Success Flag','Result Flag','Error Reason']]
#myData=[[123,'04101996','05:58:20','Inventory','First Rule','1Sub Ctgy','Description','Attrib',file_name,1,123,'No Error']]
#write = WM.WriteModule(file_name,header_data)
#write.write(myData)
print('**************************')
#print(df['DOB'].dtype)
data={'Emp_Name':'string','Emp_Id':'string','DOB':'date'}
dataType = DTC.DataTypeCheck(df,data,'DD/MM/YYYY')
dataType.checkDataType()
