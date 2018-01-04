import time
import fcntl
import errno

x = open("file.csv",'a')
while True:
    try:
        fcntl.flock(x, fcntl.LOCK_EX | fcntl.LOCK_NB)
        x.write('12010208\n')
        break
    except IOError as e:
        # raise on unrelated IOErrors       
        if e.errno != errno.EAGAIN:
            raise
        else:
            time.sleep(0.1)


