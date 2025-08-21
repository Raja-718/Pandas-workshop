
import pandas as pd


# Step 1: Create sample DataFrame

data = {
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'Finance', 'IT'],
    'Employee': ['Ram', 'Sam', 'John', 'Ann', 'Kiran', 'Scott', 'Mike'],
    'Salary': [40000, 50000, 60000, 55000, 45000, 52000, 58000],
    'Bonus': [5000, 6000, 7000, 5500, 4000, 4800, 6200]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")


# Step 2: Group by Department and calculate SUM

group_sum = df.groupby('Department').sum(numeric_only=True)
print("Group by Department - SUM:\n", group_sum, "\n")


# Step 3: Group by Department and calculate MEAN

group_mean = df.groupby('Department').mean(numeric_only=True)
print("Group by Department - MEAN:\n", group_mean, "\n")


# Step 4: Group by Department and calculate MULTIPLE AGGREGATIONS

group_multi = df.groupby('Department').agg({
    'Salary': ['sum', 'mean', 'max'],
    'Bonus': ['mean', 'min']
})
print("Group by Department - Multiple Aggregations:\n", group_multi, "\n")


# Step 5: Group by Multiple Columns (Department + Salary > 50000 check)

df['HighSalary'] = df['Salary'] > 50000
group_multi_col = df.groupby(['Department', 'HighSalary']).count()
print("Group by Department and HighSalary:\n", group_multi_col, "\n")