import csv
import os
import fcntl
import errno
import time

class WriteModule(object):
  
    #setting up init variables
  def __init__(self,file_name,header_data): #Default quotes is none
    self.file_name = file_name
    self.header_data = header_data
    #self.myData = myData
    
    #Main Write function to write into file
  def write(self,myData):
    
    self.myData=myData
    
    t=os.path.isfile(self.file_name) #checking if file exists
    #print(t)

    if t: #file exists
        #print("File Present")
        myFile=open(self.file_name,'a')

        while True: #Loop unless broken
          try:
              fcntl.flock(myFile, fcntl.LOCK_EX | fcntl.LOCK_NB)
              writer = csv.writer(myFile)
              writer.writerows(self.myData)
              fcntl.flock(myFile, fcntl.LOCK_UN)
              break
          except IOError as e:
              # raise on unrelated IOErrors       
              if e.errno != errno.EAGAIN:
                  raise
              else:
                  time.sleep(0.1) #loop continues with sleep

    else: #file does not exist
        #print("File Absent")
        myFile=open(self.file_name,'a')

        while True: #Loop 
          try:
              fcntl.flock(myFile, fcntl.LOCK_EX | fcntl.LOCK_NB)
              writer = csv.writer(myFile)
              writer.writerows(self.header_data) #print header into new file before data
              writer.writerows(self.myData)
              fcntl.flock(myFile, fcntl.LOCK_UN)
              break
          except IOError as e:
              # raise on unrelated IOErrors       
              if e.errno != errno.EAGAIN:
                  raise
              else:
                  time.sleep(0.1) #go to sleep and continue loop
    

