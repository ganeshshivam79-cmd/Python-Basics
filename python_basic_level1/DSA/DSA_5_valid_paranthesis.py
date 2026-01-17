import re
def paran(str1):
    n1=re.sub(r'[^0-9a-zA-Z]',"",str1).lower()
    return n1==n1[::-1]

print(paran("L K L"))

"""
here ^ means onlt take that if not ignore them right
"""