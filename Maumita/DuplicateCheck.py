import ReadModule as RM
import WriteModule as WM
import pandas as pd

'''col=['Emp_Name','City']
#def Duplicate(df,col):
a = RM.ReadModule('file.csv',1,0,',','\'')
df = a.read_file(col)   #pass column names for group by
x=list(df.duplicated())
#y = df.groupby('Emp_Name','City').apply(lambda x: list(x.index))
print (x)
if True in x:
  print('Duplicate present')
else:
  print('No duplicate present')'''
#Duplicate(df,'Emp_Name')   
    
    
    
class Duplicate(object):
  def __init__(self,df,col_list=[]):
    self.col_list=col_list
    self.df= df
    
  def duplicate(self):
    #df1 = self.read_file(col_list)   #pass column names for group by
    x=list(self.df.duplicated(self.col_list))
    print (x)
    if True in x:
       print('Duplicate present')
    else:
       print('No duplicate present')
 
