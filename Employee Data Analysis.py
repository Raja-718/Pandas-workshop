import pandas as pd

# Employee dataset
data = {
    'Employee': ['Amit', 'Riya', 'Karan', 'Neha', 'John', 'Sara', 'Rahul', 'Meena'],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [50000, 60000, 65000, 70000, 55000, 62000, 52000, 71000],
    'Joining_Date': pd.to_datetime(['2020-05-01', '2019-07-15', '2021-03-10', '2018-11-20',
                                     '2022-01-12', '2019-09-25', '2021-12-05', '2017-08-14'])
}

df = pd.DataFrame(data)

# Average salary per department
avg_salary = df.groupby('Department')['Salary'].mean()

# Highest paid employee
highest_paid = df.loc[df['Salary'].idxmax()]

# Employees joined before 2020
joined_before_2020 = df[df['Joining_Date'] < '2020-01-01']

# Count of employees per department
count_dept = df['Department'].value_counts()

print("📘 Employee Data")
print(df)

print("\n💰 Average Salary per Department:")
print(avg_salary)

print("\n🏆 Highest Paid Employee:")
print(highest_paid)

print("\n📅 Employees Joined Before 2020:")
print(joined_before_2020)

print("\n📊 Employee Count per Department:")
print(count_dept)

# Save analysis report
df.to_csv("employee_analysis.csv", index=False)
