import threading
import time

def thread1():
    while True:
        time.sleep(1)
        print("thread1 poppin in")
        
def thread2():
    while True:
        time.sleep(1)
        print("thread2 tips hat")

threading.Thread(target=thread1).start()
threading.Thread(target=thread2).start()
