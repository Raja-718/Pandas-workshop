
import pandas as pd

data = {
    'Name': ['Ram', 'Sam', 'John'],
    'Age': [25, 30, 28]
}
df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)
df.to_excel("students.xlsx", index=False)
df.to_json("students.json", orient="records")

csv_df = pd.read_csv("students.csv")
excel_df = pd.read_excel("students.xlsx")
json_df = pd.read_json("students.json")

print(csv_df)
print(excel_df)
print(json_df)
