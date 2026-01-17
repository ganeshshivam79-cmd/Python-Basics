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

p1["date_str"] = pd.Timestamp.today().date()


.dt.year → Returns the year (e.g., 2021)
.dt.month → Month as a number (e.g., 7 for July)
.dt.month_name() → Method, not attribute. See methods below.
.dt.day → Day of the month (e.g., 15)
.dt.dayofweek → Day of the week as number (Monday=0, Sunday=6)
.dt.day_name() → Method
.dt.quarter → Quarter of the year (1, 2, 3, or 4)
.dt.date → Returns just the date part
.dt.time → Time part only


df["just_time"] = df["event_time"].dt.time
it will take only time from date,month column

df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=5, freq='M')
})


dates = pd.date_range(start="2025-01-01", end="2035-01-01", freq="YS")


'D' → daily
'ME' → month end
'MS' → month start
'H' → hourly
