class A:
    def sound(self):
        print("okay A")

class B(A):
    def sound(self):
        print("okay B")

class C(B):
    def sound(self):
        print("okay C")

c = C()
c.sound()
print(C.__mro__)
