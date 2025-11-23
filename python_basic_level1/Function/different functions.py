class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"__init__ called — created Person({self.name})")

    def __repr__(self):
        # Developer-friendly representation
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        # User-friendly display string
        return f"{self.name}, {self.age} years old"

    def __del__(self):
        # Called automatically when object is deleted
        print(f"__del__ called — deleting Person({self.name})")


# Inheriting from Person
class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)  # calls Person’s __init__
        self.role = role
        print(f"__init__ called — created Employee({self.name}, {self.role})")

    def __repr__(self):
        # Developer representation (overrides parent)
        return f"Employee(name='{self.name}', age={self.age}, role='{self.role}')"

    def __str__(self):
        # User-friendly display string
        return f"{self.name} works as {self.role}"


# --- MAIN ---
emp = Employee("Shivam", 28, "Data Engineer")

print("\n--- Using print() ---")
print(emp)          # calls __str__

print("\n--- Using repr() ---")
print(repr(emp))    # calls __repr__

print("\n--- Deleting object ---")
del emp             # deletes variable → triggers __del__()

################################################################################
"""Inherit values from parent"""
class Parent:
    def __init__(self):
        self.name = "Ram"
        self.city = "Chennai"

class Child(Parent):
    def __init__(self):
        super().__init__()   # initialize Parent attributes
        # now values from parent are available
        print("From parent:", self.name, self.city)
        self.age = 25

c = Child()
print(c.name)
################################################################################e)

