# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("C:/Users/HP/Downloads/projects/customers shopping behavior project-1.csv")   # make sure file name matches your CSV

# Show first 5 rows
print("First 5 rows:")
print(data.head())

# Basic info
print("\nDataset Info:")
print(data.info())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove duplicates
data = data.drop_duplicates()

# Example Analysis 1: Average spending by Gender
if 'Gender' in data.columns and 'Purchase Amount (USD)' in data.columns:
    avg_spending = data.groupby('Gender')['Purchase Amount (USD)'].mean()
    print("\nAverage Spending by Gender:")
    print(avg_spending)

    # Plot
    avg_spending.plot(kind='bar')
    plt.title("Average Spending by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Purchase Amount")
    plt.savefig("gender_spending.png")
    plt.show()
    # Male customers spend slightly more than female customers on average.

# Example Analysis 2: Top Product Categories
if 'Category' in data.columns:
    category_count = data['Category'].value_counts()
    print("\nTop Categories:")
    print(category_count)

    # Plot
    category_count.plot(kind='bar')
    plt.title("Most Popular Categories")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.savefig("category_chart.png")
    plt.show()
    #clothing and accessories are the most popular product categories.

    # Age Distribution
if 'Age' in data.columns:
    data['Age'].plot(kind='hist', bins=10)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.savefig("age_distribution.png")
    plt.show()
    # Most customers belong to the age group of 20-40.
     
    # Gender Distribution
if 'Gender' in data.columns:
    data['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Gender Distribution")
    plt.ylabel('')
    plt.savefig("gender_distribution.png")
    plt.show()
    # The dataset contains a balanced distribution of male and female customers.

    # Top 5 Items
if 'Item Purchased' in data.columns:
    data['Item Purchased'].value_counts().head(5).plot(kind='bar')
    plt.title("Top 5 Purchased Items")
    plt.xlabel("Items")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig("Top_items.png")
    

    # A few items dominate customer purchases,indicating popular trends.

    # Purchase Amount Distribution
if 'Purchase Amount (USD)' in data.columns:
    data['Purchase Amount (USD)'].plot(kind='hist', bins=10)
    plt.title("Purchase Amount Distribution")
    plt.xlabel("Amount")
    plt.show()

    # Age vs Purchase Amount
if 'Age' in data.columns and 'Purchase Amount (USD)' in data.columns:
    plt.scatter(data['Age'], data['Purchase Amount (USD)'])
    plt.title("Age vs Purchase Amount")
    plt.xlabel("Age")
    plt.ylabel("Purchase Amount")
    plt.show()
    plt.savefig("age_vs_purchase.png")
    
    # There is no strong relationship between age and purchase amount.