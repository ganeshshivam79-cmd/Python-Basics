import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "date_str": ["2023-07-01", "2022-06-15", "2023-01-10", "2021-12-31"]
})

# 1. Convert string column to datetime
df["date"] = pd.to_datetime(df["date_str"])
# 2. Extract year
df["year"] = df["date"].dt.year
# 3. Get unique years
unique_years = df["year"].unique().tolist()
print(unique_years)
df["month_name"] = df["date"].dt.month_name()
print(list(df["month_name"]))

df["day_name"] = df["date"].dt.day_name()   #monday, #tuesday

