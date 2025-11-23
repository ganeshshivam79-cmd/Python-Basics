import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print("Thread 1 acquired lock1")
        time.sleep(1)
        with lock2:
            print("Thread 1 acquired lock2")
            print("Thread 1 done")

def thread2():
    with lock2:
        print("Thread 2 acquired lock2")
        time.sleep(1)
        with lock1:
            print("Thread 2 acquired lock1")
            print("Thread 2 done")

# Start threads
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

"""
thread1 has lock1, waiting for lock2
thread2 has lock2, waiting for lock1
"""