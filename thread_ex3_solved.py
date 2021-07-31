import threading

def increment():
    global x
    x+=1
    
def thread_func(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()
        
def main():
    global x
    x=0
    
    lock = threading.Lock()
    t1 = threading.Thread(target=thread_func, args=(lock,))
    t2 = threading.Thread(target=thread_func, args=(lock,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__ == "__main__":
   for i in range(5):
      main()
      print(f"x = {x} after Iteration {i+1}")
