
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Ram', 'Sam', 'John', 'Ann'],
    'Marks': [85, 90, 75, 88]

})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Subject': ['Math', 'Science', 'English', 'History'],
    'Grade': ['B', 'A', 'C', 'B']
})

print("DataFrame 1:\n", df1, "\n")
print("DataFrame 2:\n", df2, "\n")

# Step 2: Merge with INNER JOIN (only matching IDs)

inner_merge = pd.merge(df1,df2, on ='ID', how='inner')

print("Inner Join (only common IDs):\n", inner_merge, "\n")

# Step 3: Merge with LEFT JOIN (all from df1, matching from df2)

left_join = pd.merge(df1,df2, on='ID',how='left')
print("Left Join (all rows from df1):\n", left_join, "\n")


# Step 4: Merge with RIGHT JOIN (all from df2, matching from df1)

right_join = pd.merge(df1,df2,on='ID',how='right')
print("Right Join (all rows from df2):\n", right_join, "\n")


# Step 5: Merge with OUTER JOIN (all rows from both, NaN for missing)
outer_merge = pd.merge(df1,df2, on='ID', how='outer')
print("Outer Join (all rows from both DataFrames):\n", outer_merge, "\n")


# Step 6: Concatenation Example
df3 = pd.DataFrame({
    'ID': [7, 8],
    'Name': ['Mike', 'Tom'],
    'Marks': [82, 91]
})

concat_df = pd.concat([df1, df3], axis=0)
print("Concatenation (stacking DataFrames vertically):\n", concat_df, "\n")