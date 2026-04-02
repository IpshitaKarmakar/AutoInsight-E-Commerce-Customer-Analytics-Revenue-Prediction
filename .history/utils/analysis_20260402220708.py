import matplotlib.pyplot as plt
import seaborn as sns
def explore_business_transactions(df):
    print(f"\n Analyzing sales and business patterns")

    #Top countries by revenue
    country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    country_sales[1:].plot(kind='bar')
    plt.title("Top Revenue Countries (Excluding UK for Clarity)")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45,ha='right')
    plt.tight_layout()
    plt.savefig("outputs/top_countries.png")
    plt.close()

    print("Top 10 countries revenue saved")

    #Monthly revenue trend
    df['Month']=df['InvoiceDate'].dt.to_period('M')
    monthly_revenue=df.groupby('Month')['TotalPrice'].sum()

    plt.figure(figsize=(10,5))
    monthly_revenue.plot()
    plt.title("Monthly Revenue Trend")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("outputs/monthly_revenue.png")
    plt.close()

    print("Monthly revenue trend saved")

    # 3. Monthly Sales Trend (Quantity)
    monthly_sales = df.groupby('Month')['Quantity'].sum()

    plt.figure(figsize=(10,5))
    monthly_sales.plot()

    plt.title("Monthly Sales Volume Trend")
    plt.ylabel("Quantity Sold")
    plt.tight_layout()
    plt.savefig("outputs/monthly_sales.png")
    plt.close()

    print("Monthly sales trend saved")

    #Top products 
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    top_products.plot(kind='bar')
    plt.title("Top 10 most products are sold")
    plt.ylabel("Quantity Sold")
    plt.xticks(rotation=60,ha='right')
    plt.tight_layout()
    plt.savefig("outputs/top_products.png")
    plt.close()

    print("Top products visualization saved")

    #customer purchase frequency
    customer_freq = df.groupby('CustomerID')['InvoiceNo'].nunique()
    customer_freq = customer_freq[customer_freq < customer_freq.quantile(0.99)]

    plt.figure(figsize=(8,5))
    sns.histplot(customer_freq, bins=30)

    plt.title("Customer Purchase Frequency Distribution")
    plt.xlabel("Number of Purchases")
    plt.tight_layout()
    plt.savefig("outputs/customer_frequency.png")
    plt.close()

    # 6. Revenue Distribution (NEW)
    
    customer_revenue = df.groupby('CustomerID')['TotalPrice'].sum()

    plt.figure(figsize=(8,5))
    sns.histplot(customer_revenue, bins=50)

    plt.title("Customer Revenue Distribution")
    plt.xlabel("Total Revenue per Customer")
    plt.tight_layout()
    plt.savefig("outputs/revenue_distribution.png")
    plt.close()

    print("Customer revenue distribution saved")

    #Correlation Heatmap

    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("outputs/correlation_heatmap.png")
    plt.close()

    print("Correlation heatmap saved")

    #High value customers insight
    threshold = customer_revenue.quantile(0.8)
    high_value = customer_revenue[customer_revenue > threshold]

    print("\nKey Insights:")
    print(f"\nTop 20% customers count: {len(high_value)}")
    print(f"Revenue contribution by top customers: {high_value.sum():.2f}")
