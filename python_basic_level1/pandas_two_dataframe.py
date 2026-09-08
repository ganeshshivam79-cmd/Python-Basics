

df_students = pd.DataFrame({
    "student_id": [101, 102, 103, 105],
    "name": ["Alice", "Bob", "Charlie", "David"]
})

df_marks = pd.DataFrame({
    "student_id": [101, 103],
    "marks": [80, 90]
})

check = df_marks[~df_marks["student_id"].isin(df_students["student_id"])]

print(check)