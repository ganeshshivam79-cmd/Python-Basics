df["student_name"].str.upper()
df["student_name"].str.lower()
df["student_name"].str.contains("a")
df["student_name"].str.len()

df["student_name"].sort_values()   # Series sort
df.sort_values("student_name")     # DataFrame sort
df.sort_values("student_name", inplace=True)
print(df)