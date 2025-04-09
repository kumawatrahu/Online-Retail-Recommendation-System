import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = r"D:\Project\Encrypted-Python-Chat-master\Cleaned_OnlineRetail.xlsx"

try:
    # Read the dataset
    df = pd.read_excel(file_path)
    print("✅ File loaded successfully!\n")

    # 1️⃣ Basic statistical summary
    print("📊 Basic Statistical Summary:\n")
    print(df.describe(), "\n" + "="*50 + "\n")

    # 2️⃣ Distribution of numerical variables
    num_cols = df.select_dtypes(include=['number']).columns

    # Histograms
    df[num_cols].hist(figsize=(10, 8), bins=20, edgecolor="black")
    plt.suptitle("Distribution of Numerical Variables", fontsize=15)
    plt.show()

    # Box plots for outlier detection
    plt.figure(figsize=(10, 6))
    df[num_cols].boxplot()
    plt.xticks(rotation=45)
    plt.title("Box Plot of Numerical Variables")
    plt.show()

    # 3️⃣ Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

    # 4️⃣ Distribution of categorical variables
    cat_cols = df.select_dtypes(include=['object']).columns

    for col in cat_cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(y=df[col], order=df[col].value_counts().index)
        plt.title(f"Distribution of {col}")
        plt.show()

    # 5️⃣ Feature relationships (grouped statistics)
    if 'CategoryColumn' in df.columns and 'NumericColumn' in df.columns:  # Replace with actual column names
        print("📊 Grouped Statistics:\n")
        print(df.groupby('CategoryColumn')['NumericColumn'].mean())

except Exception as e:
    print("❌ Error:", e)
