import pandas as pd

# Load the file
file_path = "D:/Project/Encrypted-Python-Chat-master/Cleaned_OnlineRetail.xlsx"

try:
    # Read the dataset
    df = pd.read_excel(file_path)
    print("✅ File loaded successfully!\n")

    # Display basic info about the dataset
    print("📌 Dataset Info:")
    print(df.info())
    print("\n" + "="*50 + "\n")

    # Display shape of the dataset
    print(f"📊 Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
    print("\n" + "="*50 + "\n")

    # Summary statistics for numerical columns
    print("📈 Summary Statistics:")
    print(df.describe())
    print("\n" + "="*50 + "\n")

    # Checking unique values in each column
    print("🔢 Unique Value Counts per Column:")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")

    print("\n" + "="*50 + "\n")

    # Checking for missing values
    print("❓ Missing Values in Each Column:")
    print(df.isnull().sum())
    print("\n" + "="*50 + "\n")

    # Checking for duplicate rows
    duplicate_rows = df.duplicated().sum()
    print(f"📌 Duplicate Rows: {duplicate_rows}")

except Exception as e:
    print("❌ Error:", e)
