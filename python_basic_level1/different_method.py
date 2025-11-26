class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"  # Human readable

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"  # Developer friendly

p = Person("Alice", 25)

print(p)       # Uses __str__ → Alice, 25 years old
p              # Uses __repr__ in interactive shell → Person('Alice', 25)


"""
If __str__ is not defined, print() will fall back to __repr__.
__repr__ should always try to give a representation that could recreate the object.
__str__ is for easy reading, __repr__ is for debugging/development.
__del__ is deleting object not for tor attibutes
"""

class Person:
    def __init__(self, name):
        self.name = name
        self.data = [1, 2, 3]
    
    def __str__(self):
        return self.name+" okay"
    
    def key1(self):
        self.v1=10


p = Person("Alice")
print(p)
 # Alice is being destroye
print(p.data)