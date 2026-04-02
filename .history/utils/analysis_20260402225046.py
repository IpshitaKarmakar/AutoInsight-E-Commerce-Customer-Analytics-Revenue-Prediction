import matplotlib.pyplot as plt
import seaborn as sns
def explore_business_transactions(df):
    print(f"\n Analyzing sales and business patterns")

    #Top countries by revenue(Excluding UK)
    country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    country_sales[1:].plot(kind='bar')
    plt.title("Top Revenue Countries (Excluding UK)")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45,ha='right')
    plt.tight_layout()
    plt.savefig("outputs/top_countries.png",dpi=300)
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
    plt.savefig("outputs/monthly_revenue.png",dpi=300)
    plt.close()

    print("Monthly revenue trend saved")

    #Top products 
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    top_products.plot(kind='bar')
    plt.title("Top 10 most products are sold")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")
    plt.xticks(rotation=60,ha='right')
    plt.tight_layout()
    plt.savefig("outputs/top_products.png",dpi=300)
    plt.close()

    print("Top products visualization saved")

    #Customer purchase frequency
    customer_freq = df.groupby('CustomerID')['InvoiceNo'].nunique()
    customer_freq = customer_freq[customer_freq < customer_freq.quantile(0.99)]

    plt.figure(figsize=(8,5))
    sns.histplot(customer_freq, bins=50)

    plt.title("Customer Purchase Frequency Distribution")
    plt.xlabel("Number of Purchases")
    plt.ylabel("Number of Customers")
    plt.xlim(0,30)
    plt.tight_layout()
    plt.savefig("outputs/customer_frequency.png",dpi=300)
    plt.close()


    #Correlation Heatmap

    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("outputs/correlation_heatmap.png",dpi=300)
    plt.close()

    print("Correlation heatmap saved")

    #High value customers insight
    customer_revenue=df.groupby('CustomerID')['TotalPrice'].sum()
    threshold=customer_revenue.quantile(0.8)
    high_value=customer_revenue[customer_revenue>threshold]
    print("\nKey Insights:")
    print(f"\nTop 20% customers count: {len(high_value)}")
    print(f"Revenue contribution by top customers: {high_value.sum():.2f}")
