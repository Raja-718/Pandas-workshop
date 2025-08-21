
import pandas as pd

# Sample sales dataset
data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Headphones', 'Phone', 'Tablet', 'Laptop'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics', 'Electronics', 'Electronics'],
    'Quantity': [2, 5, 3, 1, 10, 4, 2, 3],
    'Price': [60000, 20000, 15000, 60000, 2000, 20000, 15000, 60000]
}

df = pd.DataFrame(data)

# Calculate total sales amount
df['Total'] = df['Quantity'] * df['Price']

# Total sales revenue
total_revenue = df['Total'].sum()

# Sales by product
sales_by_product = df.groupby('Product')['Total'].sum().sort_values(ascending=False)

# Sales by category
sales_by_category = df.groupby('Category')['Total'].sum()

# Best-selling product (by revenue)
best_seller = df.groupby('Product')['Total'].sum().idxmax()

print("📊 Sales Data")
print(df)

print("\n💰 Total Revenue:", total_revenue)

print("\n📦 Sales by Product:")
print(sales_by_product)

print("\n📂 Sales by Category:")
print(sales_by_category)

print("\n🏆 Best Selling Product (by revenue):", best_seller)

# Save sales report
df.to_csv("sales_report.csv", index=False)
