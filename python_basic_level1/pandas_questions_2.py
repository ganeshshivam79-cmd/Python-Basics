""""
Tasks:
Read the CSV file.
Replace all null Marks with 0.
Convert Grade_Date to datetime.
Create a new column Status:
'Pass' if marks >= 40
'Fail' if marks < 40
Group by Subject and show average marks.
Export the cleaned data to cleaned_students.csv.
"""""

import pandas as pd

# 1. Read the CSV file
df = pd.read_csv("students.csv")
# 2. Fill missing marks with 0
df["Marks"].fillna(0, inplace=True)
# 3. Convert Grade_Date to datetime
df["Grade_Date"] = pd.to_datetime(df["Grade_Date"], format="%d/%m/%y")
# 4. Add Pass/Fail status
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
# 5. Group by Subject and calculate average marks
subject_avg = df.groupby("Subject")["Marks"].mean().reset_index(name="Average_Marks")
# 6. Save the cleaned DataFrame
df.to_csv("cleaned_students.csv", index=False)
