# Experiment: Apply Functions in Pandas

import pandas as pd

# Step 1: Create a sample DataFrame
data = {
    'Name': ['Ram', 'Sam', 'John', 'Ann'],
    'Age': [25, 30, 28, 22],
    'Salary': [40000, 50000, 60000, 45000]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")

# Step 2: Using apply() - apply a function to a column
df['UpdatedSalary'] = df['Salary'].apply(lambda x: x * 1.10)
print("After apply() on Salary column:\n", df, "\n")

# Step 3: Using map() - element-wise transformation on a Series
df['NameUpper'] = df['Name'].map(str.upper)
print("After map() on Name column:\n", df, "\n")

# Step 4: Using applymap() - element-wise function applied to entire DataFrame
df_numeric = df[['Age', 'Salary']]
df_rounded = df_numeric.applymap(lambda x: round(x, -3))
print("After applymap() on numeric columns:\n", df_rounded, "\n")
