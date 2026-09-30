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
df["student_id"] = df["student_id"].ffill()  
df["name"].fillna("name1", inplace=True)

df.dropna(subset=[], inplace=True)
df["name"].fillna("name1", inplace=True)
df["student_id"] = df["student_id"].ffill() -- it will fill nan with previous value
df.groupby("name")["marks"].cumsum()
Name	Marks	Group_Marks
A	3	3
A	2	5
B	1	1
B	10	11

####################################################################################
Sept 30

Assisgn a datatype of id to datatype of marks
df["marks"] = df["marks"].astype(df["student_id"].dtype) and dnot add df["marks"].dtype= by mistake
df["marks"] = df["marks"].astype(df["student_id"].dtype) -- it  is correct format and dtypes for all df.dttypes

df["city"].memory_usage(deep=True)
df.memory_usage(deep=True).sum()


df["city"] = df["city"].astype("category")


df["city"] = pd.Categorical(df["city"], categories=["Bangalore", "Mumbai","Delhi"], ordered=True)
df.sort_values(by=["city"], inplace=True


pd.api.types.is_categorical_dtype() is the correct function to check if a column is categorical.


print(df["city"].memory_usage(deep=True)) -- memory usage

zip the function


df["marks"] = df["marks"].fillna(df["student_id"])
df["marks"] = df["marks"].fillna(df["student_id"].ffill()) if amrks is null it will take previous value of student_id correct?

df["year"].ffill()    # Forward fill (use previous value)
df["year"].bfill()    # Backward fill (use next value)
df["year"].fillna(0)  # Fill with specific value

nw.dropna(how="all", axis=1, inplace=True)  -- #This code drops entire columns where ALL values are NaN.
nw.dropna(how="any", axis=1, inplace=True)  -- #This code drops entire columns where ALL values are NaN.

nw.dropna(how="all", axis=0, inplace=True)  -- #This code drops entire rows where All values are NaN.
nw.dropna(how="any", axis=0, inplace=True)  -- #This code drops entire rows where Any values are NaN.

nw.dropna(subset=["sport","age"], how="all", inplace=True)
nw.dropna(subset=["sport","age"], how="any", inplace=True)
Both will drop rows correct one is all should be None and other any can be none. if we didnt give how it takes as any

nw.duplicated()
find duplicates 
nw.duplicated().sum()

nw.drop_duplicates(subset=["value","id"], inplace=True) -- remove duplicates from these columns

d1=nw.drop_duplicates(subset=["value","id"]) or d1= nw.drop_duplicates(subset=["value","id"], keep="first")

result = nw.duplicated(subset=["value","id"], keep="first")
print(result)  the first value here doesnt appear as it is takesn as False 
nw=nw.loc([result,:])
df.loc[(df["age"]==18) ,"sector"]=7
df=df.loc[(df["age"]==18) & (df["id"]>10)]   
 df.loc[248,"Gender"]="Male"

result = nw.duplicated(subset=["value","id"], keep="last")
print(result)  the last value here doesnt appear as it is takesn as False 
nw=nw.loc([result,:])
duplicate value appear


result2 = df["info"].str.split(",", n=1, expand=True)
df[["first_name","last_name"]] = df["info"].str.split(",", n=1, expand=True)
######################################################################################################

df.isna().sum()



df["count"] = df.groupby("category")["amount"].transform("sum")
cumsum() add values one by one 10 one, 10+5=15 one but transform sum add all and put each same value like
15,15

(df['name'].isin(['k', 'n']), inplace=True)
df[["first_name", "last_name"]] = df["name"].str.rsplit(" ", n=1, expand=True)
