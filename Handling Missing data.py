
import numpy as np
import pandas as pd

data = {
    'Name': ['Raja','Rajesh','Rajnish',np.nan,'Shayam'],
    'Age': [ 25,26,27,np.nan,30],
    'marks':[88,28,90,np.nan,56],
}

df = pd.DataFrame(data)
#print(df)
print("Check missing values (True means missing):\n", df.isnull(), "\n")
print("Total missing values in each column:\n", df.isnull().sum(), "\n")

# Step 3: Handle missing values using fillna()
#fill NaN in age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)

# fill NAN in marks with 0
df['marks'] = df['marks'].fillna(0)

print(df)

# fill NaN in name with unknown

df['Name'] = df['Name'].fillna('Unknown')

print("DataFrame after handling missing values with fillna:\n", df, "\n")

# Re-create original DataFrame to show dropna effect
df2 = pd.DataFrame(data)
print("Dropping rows with NaN values:\n", df2.dropna(), "\n")

# Step 5: Drop columns with missing values
print("Dropping columns with NaN values:\n", df2.dropna(axis=1), "\n")