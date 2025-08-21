import pandas as pd

data = {
    'Name': ['Ram', 'Sam', 'John', 'Ann'],
    'Salary': [40000, 50000, 60000, 45000]
}
df = pd.DataFrame(data)

df['JoiningDate'] = pd.date_range(start="2022-01-01", periods=len(df), freq='M')

df['Year'] = df['JoiningDate'].dt.year
df['Month'] = df['JoiningDate'].dt.month
df['Weekday'] = df['JoiningDate'].dt.day_name()

filtered = df[df['JoiningDate'] > "2022-02-01"]
print(filtered)
