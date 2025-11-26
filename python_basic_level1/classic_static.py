
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