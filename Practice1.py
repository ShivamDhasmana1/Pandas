import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Raj", "Sneha", None],
    "Age": [22, 30, None, 28, 26],
    "City": ["Delhi", "Mumbai", "Delhi", None, "Chennai"]
}

df = pd.DataFrame(data)
print(df)


print("\nSelecting first 3 rows using iloc\n")

print(df.iloc[0:3,:])

print("\nSelecting name and city using loc\n")

print(df.loc[:,("Name" , "City")])

print("\nFiltering rows where age  > 25 :\n")
print(df[df["Age"]>25])

print("Sorting by age: \n")
print(df.sort_values(by="Age" , ascending=False))

print("Replacing missing values: \n")
print(df.isnull().sum())
print(df["Name"].fillna("Unknown"))
print(df["City"].fillna("No Provied"))
print(df["Age"].fillna(df["Age"].mean()))