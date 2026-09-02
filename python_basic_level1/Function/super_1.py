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