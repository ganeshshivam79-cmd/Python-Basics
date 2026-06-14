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
