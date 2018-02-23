##Start
import pandas as pd
import datetime as dt
from globalVar import *

class DataTypeCheck(object):
  
  def __init__(self,df,data_dict,date_format=""):
    self.df=df
    self.data_dict=data_dict
    self.date_format=date_format
    self.dataframe=pd.DataFrame()
    self.formats=[]
    self.date_dict=global_dateDict
    self.fmts=[]
    
  def checkDate(self,date):
    
    if(self.date_format):
      for key,value in self.date_dict.items():
        try:
           t=dt.datetime.strptime(date, value)
           if key not in self.formats:
            self.formats.append(key)  #change
           break
        except ValueError as err:
           self.data_format_err=1

  def checkFormat(self,fmts):
    #print(fmts)
    if(len(fmts)==0):
      print('Date format not in list')
    elif(len(fmts)>1):
      print('Multiple date formats found')
    elif(self.data_format_err==1):
      print('Date format doesnot match')
    else:
      if(fmts[0]==self.date_format):
        print('Date format matches : {0}'.format(fmts[0]))
    
  def checkDataType(self):
    
    for data in self.data_dict:
      
      if(self.data_dict[data]=='string'):
        if(self.df[data].dtype=='object'):
          print(('{0} - Matched as {1}').format(data,self.data_dict[data]))
        else:
           print(('{0} - Not Matched as {1}').format(data,self.data_dict[data]))
        
      elif(self.data_dict[data]=='number'):
        if(self.df[data].dtype=='int64'):
          print(('{0} - Matched as {1}').format(data,self.data_dict[data]))
        else:
           print(('{0} - Not Matched as {1}').format(data,self.data_dict[data]))
    
      elif(self.data_dict[data]=='decimal'):
        if(self.df[data].dtype=='float64'):
          print(('{0} - Matched as {1}').format(data,self.data_dict[data]))
        else:
           print(('{0} - Not Matched as {1}').format(data,self.data_dict[data]))
    
      elif(self.data_dict[data][0:4]=='date'):
        self.dataframe['date'] = pd.to_datetime(self.df[data])
        datatype=str(self.dataframe['date'].dtype)
        #print(str(self.df[data].dtype))
        if(len(datatype)>10):
          if(datatype[0:10]=='datetime64'):
            print(('{0} - Matched as {1}').format(data,self.data_dict[data]))
            for datesInDataframe in self.df[data]:
              for date in datesInDataframe.splitlines():
                #print(date)
                self.checkDate(date)
            #print(self.formats)
            self.checkFormat(self.formats)
          else:
            print(('{0} - Not Matched as {1}').format(data,self.data_dict[data]))
        
