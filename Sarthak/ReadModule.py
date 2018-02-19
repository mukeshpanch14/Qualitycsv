import pandas as pd
import csv

class ReadModule(object):

  ###INIT STARTS###
  
  def __init__(self,filename,header_count,footer_count,delimiter,quote=''): #Default quotes is none
    self.filename = filename
    self.header_count = header_count
    self.footer_count = footer_count
    self.delimiter = delimiter
    self.quote = quote
    
    try:
      with open(self.filename) as file:
          i=0
          for line in file.readlines():
            i=i+1
          self.count=i  #RETURNS COUNT OF ROWS

      if(self.header_count>0):
        self.header_pos = self.header_count-1 #gets the header position
      else:
        self.header_pos = -1

      if(self.footer_count>0):
        self.footer_pos=self.count - self.footer_count
      else:
        self.footer_pos = self.count
    except Exception as e:
      print('Error in class initialization : ' + str(e) )
      raise
  ###STR FUNCTION FOR PRINTING###
  
  def __str__(self):  ##Edit for print function
    return ('filename is ' + self.filename + ' with delimiter ' + self.delimiter + ' and quote : "' + self.quote + '"')
  
  ###HEADER FUNCTION TO RETURN THE HEADER###
  
  def getHeader(self):  ##Returns header as a list of columns
    
    try:
      header = []
      if(self.header_pos>=0):
        with open(self.filename) as file:
          i=0
          for line in file.readlines():
            if i == self.header_pos:  #If in header row
              header_string =line.rstrip() #strips \n 
            i=i+1
        header_list = header_string.split(self.delimiter)  #strips by delimiter
        self.header = []

        for item in header_list:
          self.header.append(item.strip(self.quote)) #header to list
    except Exception as e:
      print('Error in header function : ' + str(e) )
      raise
    return self.header
  
  ###READ FUNCTION TO RETURN THE DATAFRAME###
  def read_file(self,col_list=[],header_flag='columns'):    #No arguments needed unless specified
    
    try:
      df = pd.DataFrame()
      if len(col_list)==0 and self.header_count==0:        #Setting the arguments
        col_list = []
      elif len(col_list)==0 and self.header_count>0:
        col_list = self.getHeader()                     #Gets the header by default

      with open(self.filename) as file:
        if self.quote=='':                                  #Sets the quote
          reader = csv.reader(file, delimiter=self.delimiter)
        else:
          reader = csv.reader(file, delimiter=self.delimiter, quotechar=self.quote)

        i=0
        self.col_names=[]
        for row in reader:
          if i==self.header_pos and header_flag!='columns':   #if column postions are given
            for item in col_list:
              for q in range(len(self.getHeader())):
                if str(q) in str(item):
                  self.col_names.append(str(row[q]))
            i=i+1
          elif header_flag=='columns':
            self.col_names=col_list
      if self.quote:
        df = pd.read_csv(self.filename,skipinitialspace=True, usecols=self.col_names,quotechar=self.quote)
      else:
        df = pd.read_csv(self.filename,skipinitialspace=True, usecols=self.col_names)
      print(self.header_pos)
      print(self.footer_pos)
      return df[self.header_pos:self.footer_pos-1]
            
    except Exception as e:
      print('Error in read_file function : ' + str(e) )
      raise
