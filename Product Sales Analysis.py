import pandas as pd

# Sample product sales data
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Mar', 'Mar'],
    'Units_Sold': [50, 120, 80, 70, 150, 60, 90, 200],
    'Price_per_Unit': [60000, 20000, 15000, 60000, 20000, 15000, 60000, 20000]
}

df = pd.DataFrame(data)

# Calculate total sales
df['Total_Sales'] = df['Units_Sold'] * df['Price_per_Unit']

# Monthly sales summary
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

# Product-wise sales summary
product_sales = df.groupby('Product')['Total_Sales'].sum()

# Best selling product
best_product = product_sales.idxmax()
best_sales = product_sales.max()

# Best month for sales
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print("📘 Product Sales Data")
print(df)

print("\n📊 Monthly Sales Summary:")
print(monthly_sales)

print("\n📊 Product-wise Sales Summary:")
print(product_sales)

print(f"\n🏆 Best Selling Product: {best_product} (₹{best_sales})")
print(f"📈 Best Month for Sales: {best_month} (₹{best_month_sales})")

# Save report
df.to_csv("product_sales_analysis.csv", index=False)
