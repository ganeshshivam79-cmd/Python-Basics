class A:
    x = 10
    y = 20

obj = A()

print(getattr(obj, "x"))      # 10
print(getattr(obj, "z", 0))   # 0 (default, since z doesn't exist)
setattr(obj, "x", 25)
print(getattr(obj, "x"))  
delattr(A, "y")            # give the class name A directly and dont use variable here
print(hasattr(A, "y"))  #checks if the attribute exists.

getattr
setattr
hasattr
delattr