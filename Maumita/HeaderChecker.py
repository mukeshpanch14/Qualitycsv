import ReadModule as Read

def HeaderCheck(a):
  ReadInstance = Read.ReadModule('file.csv',1,0,',','\'')
  header = ReadInstance.header_func()
    if header==a
       print("Headers are same")
    else:
      print("Header mismatch")
      
HeaderCount=input("Enter number of Headers:")
a=[]
for i in HeaderCount:
  x=input("Enter Field name:")
  a.append(x)

HeaderCheck(a)  
  