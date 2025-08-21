import pandas as pd

# Sample student exam data
data = {
    'Student': ['Amit', 'Priya', 'Raj', 'Neha', 'Aman', 'Simran', 'Vikas', 'Anjali'],
    'Maths': [85, 92, 78, 88, 65, 95, 70, 80],
    'Science': [90, 85, 82, 91, 72, 89, 68, 76],
    'English': [78, 88, 74, 80, 69, 92, 72, 85]
}

df = pd.DataFrame(data)

# Calculate total marks
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)

# Calculate percentage
df['Percentage'] = df['Total'] / 3

# Assign grade based on percentage
def grade(p):
    if p >= 90:
        return 'A+'
    elif p >= 75:
        return 'A'
    elif p >= 60:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Percentage'].apply(grade)

# Topper
topper = df.loc[df['Percentage'].idxmax()]

# Subject-wise average
subject_avg = df[['Maths', 'Science', 'English']].mean()

print("📘 Student Exam Results Data")
print(df)

print("\n🏆 Topper of the Class:")
print(topper)

print("\n📊 Subject-wise Average Marks:")
print(subject_avg)

# Save results
df.to_csv("student_results.csv", index=False)
