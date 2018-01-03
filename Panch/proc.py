import time
import fcntl

x=open("file.csv",'w+')
while True:
    try:
        fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)
        break
    except IOError as e:
        # raise on unrelated IOErrors
        if e.errno != errno.EAGAIN:
            raise
        else:
            time.sleep(0.1)