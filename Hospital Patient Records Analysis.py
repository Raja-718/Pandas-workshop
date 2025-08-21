import pandas as pd

# Sample hospital data
data = {
    'Patient_ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['John', 'Alice', 'Bob', 'Clara', 'David', 'Ella', 'Frank'],
    'Department': ['Cardiology', 'Neurology', 'Orthopedics', 'Cardiology', 'Neurology', 'Orthopedics', 'Cardiology'],
    'Age': [45, 52, 36, 60, 41, 29, 50],
    'Bill_Amount': [50000, 70000, 30000, 45000, 60000, 25000, 55000],
    'Admission_Days': [5, 7, 3, 6, 4, 2, 8]
}

df = pd.DataFrame(data)

# Average bill per department
avg_bill = df.groupby('Department')['Bill_Amount'].mean()

# Average admission days per department
avg_days = df.groupby('Department')['Admission_Days'].mean()

# Patient with highest bill
highest_bill_patient = df.loc[df['Bill_Amount'].idxmax()]

# Department with max total revenue
dept_revenue = df.groupby('Department')['Bill_Amount'].sum()
best_dept = dept_revenue.idxmax()

print("🏥 Hospital Patient Records")
print(df)

print("\n💰 Average Bill Amount per Department:")
print(avg_bill)

print("\n🛏️ Average Admission Days per Department:")
print(avg_days)

print("\n👑 Patient with Highest Bill:")
print(highest_bill_patient)

print(f"\n🏆 Department Generating Highest Revenue: {best_dept} (₹{dept_revenue[best_dept]})")

# Save report
df.to_csv("hospital_patient_analysis.csv", index=False)
