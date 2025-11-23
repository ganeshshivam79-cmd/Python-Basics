class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

obj = B()
obj.show()          # Output: B
print(B.__mro__)    # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
