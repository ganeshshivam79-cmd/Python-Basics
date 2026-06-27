pd.concat([df1, df2])          # axis=0 default → stack rows
pd.concat([df1, df2], axis=1) # combine columns

first concat add rows one after one 
second concat combine columns  by matching Index

pd.concat([df1, df2], axis=1, join="inner")  -- inner join matching Index
pd.concat([df1, df2], axis=1, join="outer")  and pd.concat([df1, df2], axis=1)
keeps all all index and both are same 

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