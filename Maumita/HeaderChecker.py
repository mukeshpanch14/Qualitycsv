import ReadModule as Read

Class Header(object):
  def __init__(self,a,header):
    self.a=a
    self.header=header
  
  def HeaderCheck(self):
  print(header)
  print(a)
  if header==a:
       print("Headers are same")
  else:
      print("Header mismatch")