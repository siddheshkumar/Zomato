import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("zomato_sales_data.csv")

# Preview the dataset
print("Dataset Preview:\n", data.head())

# Data Summary
print("\nDataset Information:")
data.info()
print("\nSummary Statistics:\n", data.describe())

# Check for missing values
print("\nMissing Values:\n", data.isnull().sum())

# Fill or drop missing values (if any)
data = data.dropna()

# Add a new column for profit margin (%)
data['Profit Margin (%)'] = (data['Profit'] / data['Sales']) * 100

# Top 10 restaurants by total sales
top_restaurants = data.groupby('Restaurant Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Restaurants by Sales:\n", top_restaurants)

# Top 10 cities by total sales
top_cities = data.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Cities by Sales:\n", top_cities)

# Sales trend over time
data['Date'] = pd.to_datetime(data['Date'])
sales_trend = data.groupby('Date')['Sales'].sum()

# Visualization
sns.set_theme(style="whitegrid")

# Sales Trend Plot
plt.figure(figsize=(12, 6))
sales_trend.plot()
plt.title("Sales Trend Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.grid(True)
plt.show()

# Top 10 Restaurants by Sales (Bar Plot)
plt.figure(figsize=(12, 6))
top_restaurants.plot(kind='bar', color='orange')
plt.title("Top 10 Restaurants by Sales", fontsize=16)
plt.xlabel("Restaurant Name", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.show()

# Top 10 Cities by Sales (Bar Plot)
plt.figure(figsize=(12, 6))
top_cities.plot(kind='bar', color='green')
plt.title("Top 10 Cities by Sales", fontsize=16)
plt.xlabel("City", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.show()

# Profit Margin Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Profit Margin (%)'], bins=20, kde=True, color='purple')
plt.title("Distribution of Profit Margins", fontsize=16)
plt.xlabel("Profit Margin (%)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# Save cleaned dataset
cleaned_file = "zomato_cleaned_sales_data.csv"
data.to_csv(cleaned_file, index=False)
print(f"Cleaned data saved to {cleaned_file}")

# Insights
print("\nKey Insights:")
print("1. Top 10 restaurants by sales include:", list(top_restaurants.index))
print("2. Top 10 cities by sales include:", list(top_cities.index))
print("3. The average profit margin is {:.2f}%".format(data['Profit Margin (%)'].mean()))
