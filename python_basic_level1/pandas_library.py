from sqlalchemy import create_engine
import pandas as pd


# 1. Create database connection
engine = create_engine("database_connection_string")


# --------------------------------------------------
# READ FUNCTIONS (SQL → DataFrame)
# --------------------------------------------------

# Read using custom SQL query
df = pd.read_sql_query(
    "SELECT * FROM employees",
    engine
)

# Read full table directly
df = pd.read_sql_table(
    "employees",
    engine
)

# General read function (query OR table name)
df = pd.read_sql(
    "SELECT * FROM employees",
    engine
)

# Also works with table name
df = pd.read_sql(
    "employees",
    engine
)


# --------------------------------------------------
# WRITE FUNCTIONS (DataFrame → SQL)
# --------------------------------------------------

# Replace old table completely
df.to_sql(
    "employees",
    engine,
    if_exists="replace",
    index=False
)

# Append new rows
df.to_sql(
    "employees",
    engine,
    if_exists="append",
    index=False
)

# Fail if table already exists
df.to_sql(
    "employees",
    engine,
    if_exists="fail",
    index=False
)


# --------------------------------------------------
# CONNECTION FUNCTIONS
# --------------------------------------------------

# Open connection manually
conn = engine.connect()

# Execute SQL directly
conn.execute(
    "DELETE FROM employees WHERE id=10"
)

# Close engine connection
engine.dispose()


# --------------------------------------------------
# CHECK TABLES IN DATABASE
# --------------------------------------------------

from sqlalchemy import inspect

inspector = inspect(engine)

tables = inspector.get_table_names()

print(tables)


# --------------------------------------------------
# EXAMPLE FULL FLOW
# --------------------------------------------------

# Read from SQL
df = pd.read_sql_query(
    "SELECT * FROM employees",
    engine
)

# Modify dataframe
df["salary"] = df["salary"] + 1000

# Save back to SQL
df.to_sql(
    "employees",
    engine,
    if_exists="replace",
    index=False
)