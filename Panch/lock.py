import fcntl

import time
x = open('file.csv','w+')
fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)
time.sleep(60)
fcntl.flock(x, fcntl.LOCK_UN)
