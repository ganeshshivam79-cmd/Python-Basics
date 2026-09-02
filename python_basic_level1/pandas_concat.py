pd.concat([df1, df2])          # axis=0 default → stack rows
pd.concat([df1, df2], axis=1) # combine columns

first concat add rows one after one 
second concat combine columns  by matching Index

pd.concat([df1, df2], axis=1, join="inner")  -- inner join matching Index
pd.concat([df1, df2], axis=1, join="outer")  and pd.concat([df1, df2], axis=1)
keeps all index and both are same 

pd.merge(df1, df2, on="id", how="inner") 
#concat axis=1 match by index and merge match by common value

df.drop("age", axis=1)   # drop column
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