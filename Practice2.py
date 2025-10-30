import pandas as pd

df = pd.read_csv("Students.csv")
print("Showing all rows\n")
print(df)

print("Filtered students with marks ≥ 80: \n")
filtered = df[df["Marks"] >= 80]
print(filtered)

print("Sort by marks in descending order\n")
print(df.sort_values(by="Marks",ascending=False,inplace=True))
print(df.head(3))
print("\nChecking for missing values:")
if df.isnull == True:
    print("Found")
else:
    print("Not found")