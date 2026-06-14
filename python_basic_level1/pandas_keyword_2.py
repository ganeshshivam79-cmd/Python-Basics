df.head()
df.tail()
df.shape	                    "Tuple of (rows, columns)"
df.info()	                    "Column types, non-null counts, memory"
df.describe()	                "Statistical summary of numeric columns"
df.columns()
df.index()
df.dtypes
df["year"].unique()          -- 	"Returns unique values"
df["year"].nunique()         --      "Returns count of unique values"
df["name"].value_counts()    --    "Frequency of each unique value"
df.drop('unnecessary_column', axis=1, inplace=True)
df = df.drop(['col1', 'col2'], axis=1)
df2=df1.groupby("name")["id"].sum().reset_index()
print(df2)
print(type(df2))

df["row_num"] = range(1, len(df) + 1)

"""boolean"""
df.duplicated() -- boolean
df.isna()
df.notna() -- check for non nan boolean return
df["name"].str.startswith("key") -- boolean

df.dropna(subset=[], inplace=True)
df["name"].fillna("name1", inplace=True)
df["student_id"] = df["student_id"].ffill()

df.groupby("name")["marks"].cumsum()
Name	Marks	Group_Marks
A	3	3
A	2	5
B	1	1
B	10	11

df.isna().sum()

df["count"] = df.groupby("category")["amount"].transform("sum")
cumsum() add values one by one 10 one, 10+5=15 one but transform sum add all and put each same value like
15,15