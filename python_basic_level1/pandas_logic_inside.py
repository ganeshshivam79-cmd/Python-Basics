df_div7 = df[df.index % 7 == 0] #index divisible by 7
df=df[df["name"].isna()]#have only nan values

df = df.reset_index().rename(columns={"index": "old_index"}) -- index renaming 
df = df.set_index("col_name", drop=False) 
df.index=df["col_name"] --#under the difference
column is moved to index and drop=False which means still column present under column list


#constrainst
#surrogate key
#primry key in snowflake
#merge
#null handling
#left join null vlaues
#stored procedure
#functions in snowflake
#scd
#concat null


df=df[df.isna().any(axis=1)]
check for all rows and if any one cell is empty it shows all
    
    # REMOVE / MODIFY / TRANSFORM METHODS

df = df.drop_duplicates()                  
# remove duplicate rows

df = df.dropna()                          
# remove rows with NaN

df = df.drop("salary", axis=1)            
# remove column (axis=0 for row)
df = df.drop(1, axis=0)
drop the index 1

df["age"] = df["age"].fillna(0)           
# replace NaN with 0

df["city"] = df["city"].replace("NY", "New York")  
# replace values

df = df.sort_values("salary", ascending=False)      
# sort by salary descending

df = df.sort_index()                      
# sort by index

df = df.rename(columns={"old_name":"new_name"})     
# rename column

df = df.reset_index(drop=True)            
# reset index to 0,1,2...

df = df.set_index("emp_id")               
# make emp_id index

df["age"] = df["age"].astype("int")       
# change datatype

df3 = pd.merge(df1, df2, on="id", how="inner")      
# merge 2 dataframes

df3 = pd.concat([df1, df2], axis=0)       
# combine rows (axis=1 → columns)

grouped = df.groupby("department")         
# group by department

result = df.groupby("department")["salary"].sum()   
# group + aggregate

df = df.drop_duplicates(subset=["name"], keep="last")  
# remove duplicates based on name, keep last

df.loc[0,["name","age","id"]]
df.iloc[2:10, 3:5]
loc -- label based
iloc -- index based

import pandas as pd

df = pd.DataFrame({
    "name": ["ram", "john", "priya", "arun"],
    "age": [20, 25, 30, 22],
    "salary": [50000, 80000, 30000, 90000]
})


# 1. Apply on ONE COLUMN → uppercase
df["name"] = df["name"].apply(lambda x: x.upper())


# 2. Apply with IF ELSE on ONE COLUMN
df["salary_status"] = df["salary"].apply(
    lambda x: "High" if x > 60000 else "Low"
)


# 3. Apply with MULTIPLE COLUMNS (axis=1)
df["bonus"] = df.apply(
    lambda x: x["salary"]*0.10 if x["age"] > 23 else x["salary"]*0.05,
    axis=1
)


# 4. Concatenate TWO COLUMNS
df["details"] = df.apply(
    lambda x: x["name"] + "_" + str(x["age"]),
    axis=1
)


# 5. Multiple conditions (nested if else)
df["category"] = df.apply(
    lambda x: "Senior" if x["age"] > 28
              else "Mid" if x["age"] > 22
              else "Junior",
    axis=1
)


print(df)