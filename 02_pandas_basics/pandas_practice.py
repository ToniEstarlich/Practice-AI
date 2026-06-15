import pandas as pd

# load data
df = pd.read_csv("sales_data.csv")

# 1. view first rows
print(df.head())

# 2. dataset info
print(df.info())

# 3. basic statistics
print(df.describe())

# 4. filter only London
london = df[df["city"] == "London"]
print(london)

# 5. total sales (quantity * price)
df["total"] = df["quantity"] * df["price"]
print(df)

# 6. sales by city
print(df.groupby("city")["total"].sum())

# 7. most sold product
print(df.groupby("product")["quantity"].sum())