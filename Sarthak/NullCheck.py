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
      if(math.isnan(self.df[col].min())):
        print('Null')
        print(self.df[col].min())
      else:
        print('Not Null')
        print(self.df[col].min())