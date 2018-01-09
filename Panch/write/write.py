import csv
import os


header_data=[['Rule Id','Run Date','Run Time','Subject Area','Rule Name','Rule Sub Ctgy','Rule Description','Attribute Name','File Name','Success Flag','Result Flag','Error Reason']]
myData=[[123,'04101995','05:58:20','Inventory','First Rule','1Sub Ctgy','Description','Attrib','File_name',1,123,'No Error']]

file_name='write_out.csv'
t=os.path.isfile('write_out.csv')
print(t)

if t:
    print("Fijle Present")
    myFile=open(file_name,'a')
    writer = csv.writer(myFile)
    writer.writerows(myData)
else:
    print("File Absent")
    myFile=open(file_name,'a')
    writer = csv.writer(myFile)
    writer.writerows(header_data)
    writer.writerows(myData)

    


