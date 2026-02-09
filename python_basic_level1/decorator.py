"""
In Python, a decorator is a powerful and elegant way to modify or extend the behavior of
 functions or methods without altering their actual code. It is essentially a function that takes
  another function as an argument and returns a new function with enhanced functionality. 
"""


def decorator(func):
    def wrapper():
        print("This is data")
        func()
        print("No data")
    return wrapper


@decorator
def say_hello():
    print("I am Mahesh")

print(say_hello())