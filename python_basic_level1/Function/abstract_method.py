from abc import ABC, abstractmethod

# Defining an abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Subclass inheriting from abstract class
class Dog(Animal):
    def sound(self):
        return "Bark!"  # Dog provides implementation for the abstract method

# Another subclass
class Cat(Animal):
    def sound(self):
        return "Meow!"  # Cat also provides its own implementation

# Both Dog and Cat have implemented the abstract method, so you can create instances
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark!
print(cat.sound())  # Output: Meow!
"""
An abstract method is a method that is declared but not given any implementation (body).
It simply defines what a method should do, not how it does it.
The actual implementation is provided by a subclass (child class).
"""