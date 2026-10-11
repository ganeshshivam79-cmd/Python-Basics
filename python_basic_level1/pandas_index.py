import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 2, 3],
    'name': ['A', 'B', 'D', 'C']
})

df1=df.copy()
# Correct way - just use set_index directly
df = df.set_index("id", drop=False)
print(df)
df=df.reset_index(drop=True) #because it already there in columns so it will give error
print(df)

#the column changed to index and dropped form columns
df1 = df1.set_index("id")
print(df1)
df2=df1.reset_index()
print(df1)
# the indexed column will not be dropped
df3=df1.reset_index(drop=True)
print(df3)
