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



