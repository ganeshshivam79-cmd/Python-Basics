Method	                                 Description
df.dropna(inplace=True)	                Drops rows with NaN
df.fillna(value, inplace=True)	        Fills NaNs with a value
df.drop(columns, inplace=True)	        Drops specific columns
df.rename(columns=..., inplace=True)	Renames columns
df.sort_values(..., inplace=True)	    Sorts the DataFrame
df.reset_index(inplace=True)	        Resets the index



df.dropna(subset=["value"], inplace=True)
df.drop_duplicates(subset=['data'], inplace=True)

df[filter condition should be like that not removing ones]
subset is most for drop, dropna, drop_duplicates(), fillna but fillna needs to have methods


