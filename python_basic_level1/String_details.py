all(ch in s2 for ch in s1)
a=b.count('python') == count objects

re.fullmatch(r'[^a-zA-Z0-9\s]+', '@#')   # True
re.fullmatch(r'[^a-zA-Z0-9\s]+', '@')    # True
re.fullmatch(r'[^a-zA-Z0-9\s]+', '')     # False
r'[^a-zA-Z0-9\s]+' -- ignore charcyer, number, spaces and check and give result 

d=re.sub(r'[^a-zA-Z0-9]','',"da gh @#")
print -- dagh


import re

text = "abc@123"

result = re.search(r'[^a-zA-Z0-9]', text)
print(result is not None)
check pnly spcial charcter is there it will retyurm True

from collections import Counter

counts = Counter(ch.lower() for ch in text if ch.lower() in "aeiou")
print(counts)


text = "2024-09-01-report"
print(text.rpartition("-"))  #('2024-09-01', '-', 'report')
print(text.partition("-"))
('2024', '-', '09-01-report')

str1 = "PyNaTive"

lowercase = ''.join(ch for ch in str1 if ch.islower())
uppercase = ''.join(ch for ch in str1 if ch.isupper())