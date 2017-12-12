import pandas as pd
import csv

class ReadModule(object):
    
  def __init__(self,filename,header_count,footer_count,delimiter):
    self.filename = filename
    self.header_count = header_count
    self.footer_count = footer_count
    self.delimiter = delimiter
    
    with open(self.filename) as file:
        i=0
        for line in file.readlines():
          i=i+1
        self.count=i
      
    if(self.header_count>0):
      self.header_pos = self.header_count-1 #gets the header position
    else:
      self.header_pos = -1
    
    if(self.footer_count>0):
      self.footer_pos=self.count - self.footer_count
    else:
      self.footer_pos = self.count
    print(self.footer_pos)
    #if(self.footer_count>0):
     # self.footer_pos = self.footer_count-1 #gets the footer position
    #else:
    #  self.footer_pos = -1
    
  def __str__(self):
    return ('filename is '+ '"' + self.filename+'"' + ' with delimiter : '+'"' + self.delimiter + '"')
  
  def header(self):
    header = []
    if(self.header_pos>=0):
      with open(self.filename) as file:
        i=0
        for line in file.readlines():
          if i == self.header_pos:
            header_string= line.rstrip()
          i=i+1
      self.header = header_string.split(self.delimiter)
    return self.header
  
  def read_file(self): #edit
    df = pd.DataFrame()
    with open(self.filename) as file:
      reader = csv.reader(file, delimiter=self.delimiter, quotechar="'")
      i=0
      for row in reader:
        #print(self.footer_pos)
        if i>self.header_pos and i<self.footer_pos:
          df = df.append(pd.Series(row),ignore_index=True)
        i=i+1
    print(df)
    
a = ReadModule('file.csv',2,2,',')
#print(a)
header = a.header()
#print(header)
#a.count()
a.read_file()


