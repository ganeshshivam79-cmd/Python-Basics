import pandas as pd

data = {
    "Name": ["Velan", "Hero"],
    "Title": ["Mr. Smith", "Ms. Johnson"]
}

df = pd.DataFrame(data)
# Check if "mr" is in the DataFrame
contains_mr = (df.isin(["mr"]).any().any())

print(contains_mr)  # This will return True or False

val = df["age"].isin([19]).any()
#only one any needed if we given column name

df['Age'] = df['Age'].apply(lambda x: x + 1)
df['Name'] = df['Name'].map(lambda x: x.upper())

import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Role": ["A", "B", "C"]
}

df = pd.DataFrame(data)

# Create a mapping dictionary

role_mapping = {
    "A": "Admin", "B": "User",
    "C": "Guest"}
# Use map to replace Role codes with names
df['Role'] = df['Role'].map(role_mapping)

print(df)

df['Name'] = df['Name'].map(lambda x: x.upper())
df[cols_to_upper] = df[cols_to_upper].applymap(lambda x: x.upper())


print(df)

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22]
}

df = pd.DataFrame(data)
 # Check if 'Alice' is in the DataFrame
contains_alice = df.isin(["Alice"]).any().any()
print(contains_alice)  # Output: True

import pandas as pd

# Create DataFrame
k = {"Name": ["Hero", "Jk"], "stad": [1, 2]}
df = pd.DataFrame(k)
print(df)

# Check if 'Hero' is in any cell of the DataFrame
contain = df.isin(['Hero']).any().any()
print(contain)

# Apply lambda function to each element in the 'stad' column
lamb = df["stad"].apply(lambda x: x + 6)
print(lamb)

Convert
datatype
of
columns

# Convert 'Name' (which is currently a string) to int
df['Name'] = df['Name'].astype(int)
# Convert 'stad' (which is currently an integer) to string
df['stad'] = df['stad'].astype(str)

Map: Mapping, used
for dictionary, series or function.-- good for single column

Apply: used
for rows and columns, -- used for multiple columns

#Convert the dataframe without index:

print(df.to_string(index=False))

val = df["age"].isin([19, 20]).any()

result = pd.merge(df1, df2, left_on='emp_id', right_on='id', how='inner')
# join two different tables with different column name

concate two tables with same column name

result = pd.concat([df1, df2], ignore_index=True)
# need ignore index are else they aligned differently
convert a colu mn into list

# Convert 'Name' column (string type) into a list
name_list = df['Name'].tolist()

print(name_list)