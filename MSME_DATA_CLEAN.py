import pandas as pd

# Load the dataset
file_path = "D:\\MSME\\OnlineRetail (1).xlsx"
df = pd.read_excel(file_path)

# Display basic info
print(df.info())

# Display first few rows
df.head()

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing CustomerID (since it's important for analysis)
df = df.dropna(subset=['CustomerID'])

# Optionally, fill missing Description with "Unknown"
df['Description'] = df['Description'].fillna("Unknown")

print("Missing values handled.")

# Remove duplicate rows
df = df.drop_duplicates()

print("Duplicates removed.")

# Remove negative quantities (returns)
df = df[df['Quantity'] > 0]

# Remove transactions with zero or negative price
df = df[df['UnitPrice'] > 0]

print("Invalid data removed.")

# Save cleaned data
cleaned_file_path = "D:\MSME\Cleaned_OnlineRetail.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned dataset saved at: {cleaned_file_path}")
