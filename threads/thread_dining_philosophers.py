
import threading
import random
import time

class DiningPhilosopher(threading.Thread):

    running = True
    
    def __init__(self, name, leftFork, rightFork):
        threading.Thread.__init__(self)
        self.name = name
        self.leftFork = leftFork
        self.rightFork = rightFork
        
    def run(self):
        while (self.running):
            time.sleep( random.uniform(3,13) )
            print(f"{self.name} is hungry")
            self.dine()
    
    def dine(self):
        fork1, fork2 = self.leftFork, self.rightFork
        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print(f"{self.name}")
            fork1, fork2 = fork2, fork1
        else:
            return
                
        self.dining()
        fork2.release()
        fork1.release()
    
    def dining(self):
        print(f"{self.name}")
        time.sleep(random.uniform(1,10))
        print(f"{self.name} finishes eating and now thinking")
    
def Dining_Philosophers():
    num_of_philosopher = 5
    forks = [threading.Lock() for n in range(num_of_philosopher)]
    philosopher_names = [f"Phil{n}" for n in range(num_of_philosopher)]
    
    philosophers = [ DiningPhilosopher(philosopher_names[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]
    
    random.seed()
    DiningPhilosopher.running = True
    for p in philosophers: p.start()
    time.sleep(30)
    DiningPhilosopher.running = False
    print("It is finishing")
    
Dining_Philosophers()

