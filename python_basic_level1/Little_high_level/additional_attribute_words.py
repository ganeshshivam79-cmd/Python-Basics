class Person:
    species = "Human"  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Create instance
p = Person("Alice", 25)

# ---------------------------
# dir() → list all attributes/methods
print("dir(p):", dir(p))

# vars() → show instance attributes only
print("vars(p):", vars(p))

# isinstance() → check object type
print("isinstance(p, Person):", isinstance(p, Person))
print("isinstance(p, dict):", isinstance(p, dict))

# ---------------------------
# You can also dynamically access class attributes using getattr
print("getattr(p, 'name'):", getattr(p, "name"))

isinstance() cannot take a class as the first argument expecting subclass check.
issubclass() cannot take an instance as the first argument — it must be a class.
