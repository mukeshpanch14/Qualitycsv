import filelock
lock=filelock.FileLock("file.csv")

with lock:
    x=lock.is_locked
    print(x)

#lock.release()
##print(lock.is_locked)