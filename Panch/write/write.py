import csv
import os
import fcntl
import errno

file_name='write_out.csv'
header_data=[['Rule Id','Run Date','Run Time','Subject Area','Rule Name','Rule Sub Ctgy','Rule Description','Attribute Name','File Name','Success Flag','Result Flag','Error Reason']]
myData=[[123,'04101996','05:58:20','Inventory','First Rule','1Sub Ctgy','Description','Attrib',file_name,1,123,'No Error']]


t=os.path.isfile('write_out.csv')
print(t)

if t:
    print("File Present")
    myFile=open(file_name,'a')
    
    while True:
    try:
        fcntl.flock(myFile, fcntl.LOCK_EX | fcntl.LOCK_NB)
        writer = csv.writer(myFile)
        writer.writerows(myData)
        fcntl.flock(myFile, fcntl.LOCK_UN)
        break
    except IOError as e:
        # raise on unrelated IOErrors       
        if e.errno != errno.EAGAIN:
            raise
        else:
            time.sleep(0.1)
else:
    print("File Absent")
    myFile=open(file_name,'a')
    
    while True:
    try:
        fcntl.flock(myFile, fcntl.LOCK_EX | fcntl.LOCK_NB)
        writer = csv.writer(myFile)
        writer.writerows(header_data)
        writer.writerows(myData)
        fcntl.flock(myFile, fcntl.LOCK_UN)
        break
    except IOError as e:
        # raise on unrelated IOErrors       
        if e.errno != errno.EAGAIN:
            raise
        else:
            time.sleep(0.1)
    

