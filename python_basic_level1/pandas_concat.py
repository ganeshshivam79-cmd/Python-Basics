pd.concat([df1, df2])          # axis=0 default → stack rows
pd.concat([df1, df2], axis=1) # combine columns

first concat add rows one after one 
second concat combine columns  by matching Index

pd.concat([df1, df2], axis=1, join="inner")  -- inner join matching Index
pd.concat([df1, df2], axis=1, join="outer")  and pd.concat([df1, df2], axis=1)
keeps all all index and both are same 

df.drop("age", axis=1)   # drop column
df.drop(0, axis=0)       # drop row index 0