import threading

def count():
    x = 0
    for _ in range(10**7):
        x += 1

thread1 = threading.Thread(target=count)
thread2 = threading.Thread(target=count)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

"""GIL stands for Global Interpreter Lock. 
"""It's a concept in CPython (the default and most widely used implementation of Python).