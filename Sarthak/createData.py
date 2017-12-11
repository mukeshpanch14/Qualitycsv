from random import *
import random
import string
file = open('data.csv', 'w')
input=int(input('Please input amount of rows : '))
for p in range(input):
  z=''
  for i in range(5):
    y=random.choice(string.ascii_letters)
    z=z+y
  x=randint(1000000,99999999)
  u=str(x)
  v=str(x/7)
  data=u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+u+','+z+','+v+'\n'
  file.write(data)
file.close()