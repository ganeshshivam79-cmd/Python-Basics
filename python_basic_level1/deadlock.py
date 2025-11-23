
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()



def thread1():
    with lock1:
        print("Thread 1 acquired lock1")
        with lock2:
            print("Thread 1 acquired lock2")
            print("Thread 1 done")



def thread2():
    with lock1:
        print("Thread 2 acquired lock2")
        with lock2:
            print("Thread 2 acquired lock1")
            print("Thread 2 done")


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)



t1.start()
t2.start()
t1.join()
t2.join()


"""see if lock2 locks 1 or lock1 locks lock2 deadlock will happen but when you execute 
in compiler, 
sometimes 1 will run and generate output but this is code for dealock1"""