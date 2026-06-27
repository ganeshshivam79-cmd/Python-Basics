# ---------------- PYTHON ----------------

# Decorator
def deco(func):
    def wrapper():
        print("before"); func(); print("after")
    return wrapper

@deco
def hello(): print("hi")

# Generator
def gen():
    for i in range(5): yield i

# Destructor
class A:
    def __del__(self): print("object deleted")

# Counter / defaultdict
from collections import Counter, defaultdict, deque
Counter("banana")
d = defaultdict(list)

# args / kwargs
def add(*args): return sum(args)
def info(**kwargs): print(kwargs["name"])

# Lambda / map / filter
square = lambda x: x*x
list(map(lambda x:x*2,[1,2,3]))
list(filter(lambda x:x>2,[1,2,3,4]))

# zip / enumerate
list(zip([1,2],["a","b"]))
for i,v in enumerate(["a","b"]): print(i,v)

# List comprehension
[i*i for i in range(5)]

# Recursion
def fact(n): return 1 if n==1 else n*fact(n-1)

# Mutable / Immutable
# mutable -> list dict set
# immutable -> int str tuple

# sort vs sorted
lst.sort()
sorted(lst)

# is vs ==
a==b      # value compare
a is b    # memory compare

# Deep copy / Shallow copy
import copy
copy.copy(x)
copy.deepcopy(x)

# Reverse / Palindrome / Anagram
s[::-1]
s == s[::-1]
sorted(s1) == sorted(s2)

# Remove duplicates
list(dict.fromkeys(lst))

# Frequency count
d={}
for i in s:
    d[i]=d.get(i,0)+1

# Second largest
sorted(set(lst))[-2]

# Exception handling
try:
    x=1/0
except:
    print("error")
finally:
    print("done")

# File handling
with open("a.txt","r") as f:
    data=f.read()

# break continue pass
# break -> stop loop
# continue -> skip iteration
# pass -> do nothing


# ---------------- OOP ----------------

# Inheritance
class Child(Parent):
    pass

# super()
super().__init__(name)

# Polymorphism
class Dog:
    def sound(self): print("bark")

# Encapsulation
class A:
    def __init__(self):
        self.__salary=5000

# Static method
@staticmethod
def add(a,b): return a+b

# Class method
@classmethod
def show(cls): print(cls)

# MRO
ClassName.__mro__


# ---------------- PANDAS ----------------

import pandas as pd

# Read file
pd.read_csv("file.csv")

# Basic info
df.head()
df.tail()
df.shape
df.columns
df.dtypes

# loc / iloc
df.loc[2:5,["name","age"]]
df.iloc[2:5,0:2]

# Missing values
df[df["name"].isna()]
df[df["name"].notna()]
df.dropna(subset=["name"])
df["age"]=df["age"].fillna(0)

# Duplicates
df[df.duplicated()]
df.drop_duplicates(subset=["name"])

# Merge / Concat
pd.merge(df1,df2,on="id",how="inner")
pd.concat([df1,df2],axis=0)

# Groupby
df.groupby("subject")["marks"].sum()

# Aggregation
df.groupby("dept")["salary"].agg(["max","mean"])

# Transform
df["total"]=df.groupby("dept")["salary"].transform("sum")

# Apply lambda
df["name"]=df["name"].apply(lambda x:x.upper())
df["bonus"]=df.apply(lambda x:x["salary"]*0.1,axis=1)

# Sorting
df.sort_values("salary")

# Index
df.set_index("id")
df.reset_index(drop=True)

# isin
df[df["id"].isin([1,2,3])]

# Counts
df["name"].value_counts()
df["name"].unique()
df["name"].nunique()

# String functions
df[df["name"].str.contains("a")]
df["name"].str.startswith("A")
df["name"].str.endswith("n")

# idxmax / idxmin
df.loc[df.groupby("subject")["marks"].idxmax()]
df.loc[df.groupby("subject")["marks"].idxmin()]

# cumsum
df.groupby("subject")["marks"].cumsum()

# Largest / Smallest
df.nlargest(3,"salary")
df.nsmallest(3,"salary")

# replace / astype / rename
df["gender"]=df["gender"].replace("M","Male")
df["age"]=df["age"].astype(int)
df.rename(columns={"name":"student_name"})

# pivot table
df.pivot_table(values="marks",index="subject",aggfunc="mean")


# ---------------- SQL ----------------

from sqlalchemy import create_engine

# Create connection
engine=create_engine("postgresql://...")

# Read SQL query
pd.read_sql_query("select * from employees",engine)

# Read SQL table
pd.read_sql_table("employees",engine)

# Write dataframe to SQL
df.to_sql("employees",engine,if_exists="replace",index=False)


# ---------------- QUICK REVISION ----------------
# decorator, generator, yield, destructor, counter, defaultdict, deque
# args kwargs lambda map filter zip enumerate
# mutable immutable deep copy shallow copy
# recursion exception handling file handling
# sort sorted is vs ==
# inheritance polymorphism encapsulation abstraction super mro
# staticmethod classmethod
# pandas loc iloc merge concat groupby agg transform apply
# duplicated drop_duplicates fillna dropna isna notna
# idxmax idxmin cumsum pivot_table
# SQLAlchemy create_engine read_sql_query read_sql_table to_sql