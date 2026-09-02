class Math:
    @staticmethod
    def add(a, b):
        return a + b

Math.add(2, 3)   # 5

class val:
    cnt=1
    @classmethod
    def val1(cls):
        cls.cnt+=1
        return cls.cnt
    
d=val.val1()
print(d)
