import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 2, 3],
    'name': ['A', 'B', 'D', 'C']
})

result = df.drop_duplicates(subset=['id'])
print(result)


df.drop_duplicates(subset=["id", "name"])
#drop duplicates combining the column

result = pd.concat([df1, df2], axis=0).reset_index(drop=True)
"joining same column with next rows and drop index so all can be 1,2,4"

result = pd.concat([df1, df2], axis=1)
"joining different column with diff name in each dataframe"

result = pd.merge(df1, df2, on='id', how='inner')
"joing on using a common column"

result = pd.merge(df1, df2, left_on='emp_id', right_on='id', how='inner')
"join if different condition is there"

df[(df['subject'] == 'English') & (df['student_name'].str.startswith('A'))]['marks']
"subject is english and student name start with A and taking marks columns"

df.sort_values(['subject', 'marks'], ascending=[True, False])

df.index = ['x1', 'x2', 'x3']
df.reset_index(inplace=True)

df.rename(columns={'index': 'student_code'}, inplace=True)

df1 = df2[['col1', 'col2']].copy()

df['column'].replace(old_value, new_value)
#for all columns it will replace
df.replace("hetre", "data", inplace=True)
#for specific columns it will replace
df["sys"].replace("hetre", "data", inplace=True)
df[["sys", "mrd"]] \


    = df[["sys", "mrd"]].replace("hetre", "data")


df['rank'] = df.groupby('subject')['marks'].rank(ascending=False)

df['marks'].min()
df=df.set_index("column1")
df.index=[0,1,2]
df = df.drop(index=range(5, 21))
df = df.drop(index=[1, 2])
 df = df.drop_duplicates(subset=['data'])
df.dropna(subset=["name"], inplace=True)

df = df[df["name"].notna()]
print(df["name"].isna())
#notna for removing None
@isna gives false when it doesnt have None value
"it will delete and whole dataframe is changed based on name column"

df.columns = df.columns.str.lower()
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "")

df = df.reset_index(drop=True)
It resets the index to default (0, 1, 2, …).


df = df.reset_index(drop=False)
convert index into a column

df['subject'].value_counts()
"give the count of values"


df["name"].fillna("hero",inplace=True)



df.fillna(method="ffill", subset=["col1", "col2"], inplace=True)


first_5_cols = df.iloc[:, :5]
"""take only first 5 columns"""
df = df.iloc[:5, :5]
"first 5 rows and 5 cols"
df = df.iloc[:5]
"""first 5 rows and all columns"""
df = df.iloc[3:8, :].reset_index(drop=True)
"""it will take 3 to 7 values and reset index to 0,1,2"""

df.iloc[:, 0]        """First column (whatever its name is)1"""

df.loc[:, "name"]              # Select the "name" column
df.loc[5, "age"]               # Value at row with index 5, column "age"
df.loc[3:5, ["name", "age"]]
df.loc[df["name"] == "Alice", "age"] = 28  # Update age where name is Alice

df.loc[(df["name"] == "ajith") & (df["mark"] > 90), "age"] = 18  # ← numeric
df["age"] = df.apply(lambda x: 18 if x["name"] == "ajith" and x["marks"] > 90 else x["age"], axis=1)


