""""
Read the data into a Pandas DataFrame.
Add a new column Total_Amount = Quantity × Price.
Fill any missing values in Price with the average price of that Product.
Convert Order_Date to datetime format.
Filter orders placed after 2022-01-01.
Group by Region and show total sales (Total_Amount) per region.
Find the top 3 products by total quantity sold.
Save the final cleaned and transformed DataFrame to sales_cleaned.csv.
"""""



import pandas as pd

# 1. Read the data
df = pd.read_csv("data1.csv")
# 2. Calculate Total Amount
df["Total_amount"] = df["price"] * df["Quantity"]
# 3. Fill missing prices with average price of the same product
df["price"] = df.groupby("Product")["price"].transform(lambda x: x.fillna(x.mean()))
# 4. Convert 'order_date' to datetime
df["order_date"] = pd.to_datetime(df["order_date"], format="%d/%m/%Y")
# 5. Filter orders after 2022-01-01
filtered_df = df[df["order_date"] > "2022-01-01"]
# 6. Group by Region and calculate total sales
region_sales = df.groupby("Region")["Total_amount"].sum()
# 7. Find top 3 products by quantity sold
top_products = df.groupby("Product")["Quantity"].sum().nlargest(3)
# 8. Save final DataFrame
df.to_csv("val.csv", index=False)
