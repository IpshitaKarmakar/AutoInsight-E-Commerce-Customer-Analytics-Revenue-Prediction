import matplotlib.pyplot as plt
import seaborn as sns
def explore_business_transactions(df):
    print(f"\n Analyzing sales and business patterns")

    #Top 10 products by sales
    country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    country_sales.plot(kind='bar')
    plt.title("Top 10 revenue-generating countries")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/top_countries.png")
    plt.close()

    print("Top 10 countries revenue saved")

    #Monthly revenue trend
    df['Month']=df['InvoiceDate'].dt.to_period('M')
    monthly_sales=df.groupby('Month')['TotalPrice'].sum()

    plt.figure(figsize=(10,5))
    monthly_sales.plot()
    plt.title("Monthly Revenue Trend")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("outputs/monthly_trends.png")
    plt.close()

    print("Monthly revenue trend saved")

    #Top products 
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    top_products.plot(kind='bar')
    plt.title("Top 10 most products are sold")
    plt.ylabel("Quantity Sold")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/top_products.png")
    plt.close()

    print("Top products visualization saved")

    #customer purchase frequency
    customer_freq = df.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False).head(10)

    plt.figure(figsize=(8,5))
    sns.histplot(customer_freq, bins=30)
    plt.title("Customer Purchase Frequency Distribution")
    plt.xlabel("Number of Purchases")
    plt.tight_layout()
    plt.savefig("outputs/customer_frequency.png")
    plt.close()

    #Correlation Heatmap

    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("outputs/correlation_heatmap.png")
    plt.close()

    print("Correlation heatmap saved")

    #High value customers insight
    customers_revenue=df.groupby('CustomerID')['TotalPrice'].sum()
    threshold=customers_revenue.quantile(0.8)

    high_value=customers_revenue[customers_revenue>threshold]

    print(f"\nTop 20% customers count: {len(high_value)}")
    print(f"Revenue contribution by top customers: {high_value.sum():.2f}")
