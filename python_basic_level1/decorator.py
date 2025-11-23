
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