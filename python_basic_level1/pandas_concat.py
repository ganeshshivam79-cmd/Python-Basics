pd.concat([df1, df2])          # axis=0 default → stack rows
pd.concat([df1, df2], axis=1) # combine columns

first concat add rows one after one 
second concat combine columns  by matching Index

pd.concat([df1, df2], axis=1, join="inner")  -- inner join matching Index
pd.concat([df1, df2], axis=1, join="outer")  and pd.concat([df1, df2], axis=1)
keeps all index and both are same 

axis=0 → rows go down ↓
axis=1 → columns go across →

join='inner' → common columns/indexes
join='outer' → all columns/indexes
----------------------------------------------------------------------------------
import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Alice", "Bob"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Age": [25, 30]
})

df5 = pd.concat([df1, df2], axis=0)
df5.reset_index(drop=True, inplace=True)

print(df5)
------------------------------------------------------------------------------------

pd.merge(df1, df2, on="id", how="inner") 
#concat axis=1 match by index and merge match by common value

pd.concat([df1, df2], axis=0, join="inner")  -- common column it takes
pd.concat([df1, df2], axis=0, join="outer")  -- all column it takes

df.drop("age", axis=1)   # d    rop column
df.drop(0, axis=0)       # drop row index 0

df.to_sql(
    "employees",
    engine,
    if_exists="replace",
    index=False
)


see concat based on index it will do if axis=0 row wise concat 
even index same one after one it will go for different datatframe and same index and column concat 
axis=1 then they join together 
but merge needed interaction . so comparing same value we can merge 

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Alice", "Bob"]
})
df2 = pd.DataFrame({
    "ID": [1, 2],
    "Age": [25, 30]
})
df5 = pd.merge(df1, df2, on="ID")
print(df5)

| Code                   | Meaning                         |
| ---------------------- | ------------------------------- |
| `axis=0, join="outer"` | Stack rows, all columns         |
| `axis=0, join="inner"` | Stack rows, common columns      |
| `axis=1, join="outer"` | Combine columns, all indexes    |
| `axis=1, join="inner"` | Combine columns, common indexes |
