class inst:
    def __init__(self, v1=0):
        self.__v1 = 10  # Private attribute

    def val(self):
        return self.__v1  # Accessing private attribute via a method

v = inst()
print(v.val())  # This works because the method val() can access the private attribute

print(v.__v1)  # This will raise an AttributeError because __v1 is private