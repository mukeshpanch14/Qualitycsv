
"""Internal package for locking files"""
import fcntl

import time
x = open('file.csv','a')
fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)
x.write('12010207\n')
time.sleep(20)

   
#to unlock-- 
fcntl.flock(x, fcntl.LOCK_UN)

