##Start
import pandas as pd

class DataTypeCheck(object):
  
  def __init__(self,df,data_dict):
    self.df=df
    self.data_dict=data_dict
    
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
        self.df[data] = pd.to_datetime(self.df[data])
        datatype=str(self.df[data].dtype)
        #print(str(self.df[data].dtype))
        if(len(datatype)>10):
          print('inloop')
          print(datatype[0:10])
          if(datatype[0:10]=='datetime64'):
            print(('{0} - Matched as {1}').format(data,self.data_dict[data]))
          else:
            print(('{0} - Not Matched as {1}').format(data,self.data_dict[data]))
        
