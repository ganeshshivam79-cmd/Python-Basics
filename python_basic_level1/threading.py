import threading
import time

def task1():
    time.sleep(5)
    print("Task 1 done")

def task2():
    print("Task 2 done")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()