
"""Internal package for locking files"""
import fcntl

import time
x = open('file.csv','w+')
fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)

time.sleep(60)
#to unlock--      fcntl.flock(d, fcntl.LOCK_UN)
