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
  
  def header_func(self):  ##Returns header as a list of columns
    
    try:
      header = []
      if(self.header_pos>=0):
        with open(self.filename) as file:
          i=0
          for line in file.readlines():
            if i == self.header_pos:  #If in header row
              header_string = line.rstrip() #strips \n 
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
        col_list = self.header_func()                     #Gets the header by default

      with open(self.filename) as file:
        if self.quote=='':                                  #Sets the quote
          reader = csv.reader(file, delimiter=self.delimiter)
        else:
          reader = csv.reader(file, delimiter=self.delimiter, quotechar=self.quote)

        i=0
        self.col_pos=[]
        for row in reader:
          if i==self.header_pos and header_flag=='columns':   #Sets columns to pick
              for item in col_list:
                for q in range(len(self.header_func())):
                  if str(row[q]) in str(item):
                    self.col_pos.append(q)
          elif header_flag!='columns':
            self.col_pos=col_list

          if i>self.header_pos and i<self.footer_pos:          #Picks data based on file
            row = list(row[r] for r in self.col_pos)
            #print(row)
            df = df.append(pd.Series(row),ignore_index=True)   #Dataframe append
          i=i+1
    except Exception as e:
      print('Error in read_file function : ' + str(e) )
      raise
    return df


