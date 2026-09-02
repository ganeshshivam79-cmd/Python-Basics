class A:
    def add(self, *args):
        return sum(args)

A().add(1, 2)
A().add(1, 2, 3) -- method overloading 


class Parent:
    def show1(self):
        print("Parent class")

class Child(Parent):
    def show1(self):
        print("child class")

d = Child()
d.show1()