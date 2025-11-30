
class D:
    v1 = 10     # class variable

    @classmethod
    def key1(cls):
        cls.v1 += 1

D.key1()
print(D.v1)


#####################
class S:
    """no self, attribute nothing works"""
    @staticmethod 
    def key1():
        print("Static method")

S.key1()


"""
A class method is a method that receives the class itself (cls) as the first argument 
instead of the object (self).

A static method is a normal function placed inside a class for organization.
It does not take self or cls, so it cannot access class or object data directly.

"""