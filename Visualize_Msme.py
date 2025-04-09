import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the results from previous step
global_popular_file = r"D:\Project\Encrypted-Python-Chat-master\Global_Popular_Items.xlsx"
country_popular_file = r"D:\Project\Encrypted-Python-Chat-master\Country_Popular_Items.xlsx"
month_popular_file = r"D:\Project\Encrypted-Python-Chat-master\Month_Popular_Items.xlsx"

try:
    # Read the Excel files
    global_popular = pd.read_excel(global_popular_file)
    country_popular = pd.read_excel(country_popular_file)
    month_popular = pd.read_excel(month_popular_file)

    ### 🔹 **1️⃣ Top 10 Most Popular Items Globally**
    plt.figure(figsize=(12, 6))
    sns.barplot(data=global_popular.head(10), x='Quantity', y='Description', palette='viridis')
    plt.xlabel("Total Quantity Sold")
    plt.ylabel("Item Description")
    plt.title("🌍 Top 10 Most Popular Items Globally")
    plt.show()

    ### 🔹 **2️⃣ Top 5 Popular Items in Each Country (For 3 Sample Countries)**
    selected_countries = country_popular['Country'].unique()[:3]  # Choose first 3 countries for visualization
    for country in selected_countries:
        plt.figure(figsize=(12, 6))
        country_data = country_popular[country_popular['Country'] == country].head(5)
        sns.barplot(data=country_data, x='Quantity', y='Description', palette='coolwarm')
        plt.xlabel("Total Quantity Sold")
        plt.ylabel("Item Description")
        plt.title(f"📍 Top 5 Popular Items in {country}")
        plt.show()

    ### 🔹 **3️⃣ Top 5 Popular Items for Each Month**
    months = sorted(month_popular['Month'].unique())
    for month in months:
        plt.figure(figsize=(12, 6))
        month_data = month_popular[month_popular['Month'] == month].head(5)
        sns.barplot(data=month_data, x='Quantity', y='Description', palette='magma')
        plt.xlabel("Total Quantity Sold")
        plt.ylabel("Item Description")
        plt.title(f"📆 Top 5 Popular Items in Month {month}")
        plt.show()

    print("✅ Data visualization completed successfully!")

except Exception as e:
    print("❌ Error:", e)
