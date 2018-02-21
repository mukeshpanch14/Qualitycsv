class Header(object):
  def __init__(self,a,header):
    self.a=a
    self.header=header
  
  def HeaderCheck(self):
     print(self.header)
     print(self.a)
     if self.header==self.a:
        print("Headers are same")
     else:
        print("Header mismatch")