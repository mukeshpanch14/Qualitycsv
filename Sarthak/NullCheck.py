import ReadModule as RM
import WriteModule as WM
import pandas as pd
import math

class NullCheck(object):
  
  def __init__(self,df,col_list=[]):
    self.col_list=col_list
    self.df= df
    
  def checkNull(self):
    i=0
    j=0
    null_lines = []
    for col in self.col_list:
      for data in self.df[col]:
        #print(data)
        if(data):
          i=i+1
          j=j+1
          null_lines.append(i)
          
        else:
          i=i+1
    if(j==0):
      print('No nulls present')
    else:
      print('Nulls present')
      print(null_lines)
      print(j)
    
