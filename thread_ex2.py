import threading
import time

count=0
lock = threading.RLock()

def thread1():
    global count
    while True:
        with lock:
            count += 1
            count -= 1

def thread2():
    global count
    while True:
        with lock:
            count += 1
            count -= 1
        
        
threading.Thread(target=thread1).start()
threading.Thread(target=thread2).start()
