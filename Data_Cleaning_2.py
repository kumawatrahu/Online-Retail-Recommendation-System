import pandas as pd

# Load the file
file_path = r"D:\Project\Encrypted-Python-Chat-master\Cleaned_OnlineRetail.xlsx"

try:
    # Read the dataset
    df = pd.read_excel(file_path)
    print("✅ File loaded successfully!\n")

    # 1️⃣ Check for missing values
    print("❓ Missing Values Before Cleaning:")
    print(df.isnull().sum(), "\n" + "="*50 + "\n")

    # Fill missing values (change strategy based on column type)
    df.fillna(method="ffill", inplace=True)  # Forward fill (change if needed)
    print("✅ Missing values handled!\n")

    # 2️⃣ Remove duplicate rows
    duplicate_count = df.duplicated().sum()
    df.drop_duplicates(inplace=True)
    print(f"✅ Removed {duplicate_count} duplicate rows!\n")

    # 3️⃣ Convert data types (modify as per dataset)
    if 'DateColumn' in df.columns:  # Replace 'DateColumn' with actual column name
        df['DateColumn'] = pd.to_datetime(df['DateColumn'])
        print("✅ Date column converted to datetime!\n")

    # 4️⃣ Detect & handle outliers (IQR method)
    if 'NumericColumn' in df.columns:  # Replace with actual column name
        Q1 = df['NumericColumn'].quantile(0.25)
        Q3 = df['NumericColumn'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outlier_count = ((df['NumericColumn'] < lower_bound) | (df['NumericColumn'] > upper_bound)).sum()
        df = df[(df['NumericColumn'] >= lower_bound) & (df['NumericColumn'] <= upper_bound)]
        print(f"✅ Removed {outlier_count} outliers!\n")

    # 5️⃣ Standardize text data (remove extra spaces, convert to lowercase)
    text_columns = ['CategoryColumn']  # Replace with actual text column names
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].str.strip().str.lower()
    print("✅ Text data standardized!\n")

    # Save cleaned data
    cleaned_file_path = r"D:\Project\Encrypted-Python-Chat-master\Cleaned_OnlineRetail.xlsx"
    df.to_excel(cleaned_file_path, index=False)
    print(f"✅ Cleaned data saved to {cleaned_file_path}!")

except Exception as e:
    print("❌ Error:", e)
