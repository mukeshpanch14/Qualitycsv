import ReadModule as RM
import WriteModule as WM
import pandas as pd
import math
import WriteModule as WM
from globalVar import *

class NullCheck(object):
  
  def __init__(self,df,col_list=[]): #dataframe and column list to check for nulls
    self.col_list=col_list
    self.df= df
    self.header = global_header
    #header = [['Rule Id','Run Date','Run Time','Subject Area','Rule Name','Rule Sub Ctgy','Rule Description','Attribute Name','File Name','Success Flag','Result Flag','Error Reason']]
    self.writeModule = WM.WriteModule('write_out.csv',self.header)
        
  def checkNull(self):
    i=0
    j=0
    null_lines = []
    for col in self.col_list:
      if(math.isnan(self.df[col].min())):  #datafrane function
        ####ADD LINE NUMBER###
        self.writeModule.write([['1,Nulls are present']])
        print(self.df[col].min())   #remove prints to writemodule
      else:
        self.writeModule.write([['1,Nulls are not present']])
        print(self.df[col].min())   #remove prints to writemodule