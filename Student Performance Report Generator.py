import pandas as pd

# Sample student dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Math': [85, 67, 90, 45, 76, 59],
    'Science': [78, 72, 88, 54, 69, 60],
    'English': [92, 65, 80, 50, 72, 55]
}

df = pd.DataFrame(data)

# Calculate total and average marks
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1).round(2)

# Assign grades based on average
def grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Average'].apply(grade)

# Find top 3 students per subject
top_math = df.nlargest(3, 'Math')[['Name', 'Math']]
top_science = df.nlargest(3, 'Science')[['Name', 'Science']]
top_english = df.nlargest(3, 'English')[['Name', 'English']]

print("📌 Student Performance Report")
print(df)

print("\n🏆 Top 3 Students in Math:")
print(top_math)

print("\n🏆 Top 3 Students in Science:")
print(top_science)

print("\n🏆 Top 3 Students in English:")
print(top_english)

# Export final report
df.to_csv("student_report.csv", index=False)
