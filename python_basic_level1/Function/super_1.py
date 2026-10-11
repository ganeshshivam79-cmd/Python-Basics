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

#######################################################################################

class Data:
    def __init__(self, k):
        self.k = k + 10
    
    def val(self):
        print("okay")

class Data1(Data):
    def __init__(self, k):
        print(k)
        super().__init__(k)  # ✅ Fixed - remove 'self'
        print("yes", self.k)

d = Data(10)
d.val()  # Output: okay

d = Data1(10)

# Output:
# 20
# yes 30

##########################################
