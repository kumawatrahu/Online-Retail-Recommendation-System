import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the cleaned dataset
file_path = r"D:\Project\Encrypted-Python-Chat-master\Cleaned_OnlineRetail.xlsx"

try:
    # Read the dataset
    df = pd.read_excel(file_path)
    print("✅ File loaded successfully!\n")

    # 1️⃣ Handling missing values
    df.fillna({
        col: df[col].mean() if df[col].dtype in ['int64', 'float64'] else df[col].mode()[0]
        for col in df.columns
    }, inplace=True)

    print("✅ Missing values handled!\n")

    # 2️⃣ Feature transformation: Encoding categorical variables
    cat_cols = df.select_dtypes(include=['object']).columns
    le = LabelEncoder()

    for col in cat_cols:
        df[col] = df[col].astype(str)  # Convert to string
        df[col] = le.fit_transform(df[col])  # Apply encoding

    print("✅ Categorical variables encoded!\n")

    # 3️⃣ Feature scaling (optional: if needed for ML models)
    num_cols = df.select_dtypes(include=['number']).columns
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    print("✅ Numerical features scaled!\n")

    # 4️⃣ Feature creation: Example (Extracting year & month from a date column if it exists)
    if 'InvoiceDate' in df.columns:
        df['Year'] = pd.to_datetime(df['InvoiceDate']).dt.year
        df['Month'] = pd.to_datetime(df['InvoiceDate']).dt.month
        print("✅ New features 'Year' and 'Month' created!\n")

    # Save the transformed dataset
    output_path = r"D:\Project\Encrypted-Python-Chat-master\MSME_FEATURED_DATA.xlsx"
    df.to_excel(output_path, index=False)
    print(f"🚀 Feature engineering completed! Data saved to {output_path}")

except Exception as e:
    print("❌ Error:", e)
