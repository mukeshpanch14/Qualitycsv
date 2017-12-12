import pandas as pd
import csv

class ReadModule(object):
    
  def __init__(self,filename,header_count,footer_count,delimiter):
    self.filename = filename
    self.header_count = header_count
    self.footer_count = footer_count
    self.delimiter = delimiter
      
    if(self.header_count>0):
      self.header_pos = self.header_count-1 #gets the header position
    else:
      self.header_pos = -1
    
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
    
  def read_file(self):
    df = pd.DataFrame()
    with open(self.filename) as file:
      reader = csv.reader(file, delimiter=',', quotechar="'")
      i=0
      for row in reader:
        if i!=self.header_pos:
          df = df.append(pd.Series(row),ignore_index=True)
        i=i+1
    print(df)
    
a = ReadModule('file.csv',0,0,',')
#print(a)
header = a.header()
print(header)
a.read_file()