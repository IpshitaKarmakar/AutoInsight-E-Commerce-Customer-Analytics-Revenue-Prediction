import matplotlib.pyplot as plt

def explore_business_transactions(df):
    print(f"\n Analyzing sales and business patterns")
    # Top countries by sales
    country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

    plt.figure()
    country_sales.plot(kind='bar')
    plt.title('Top revenue-generating countries')
    plt.xticks(rotation=45)
    plt.savefig("outputs/country_sales.png")

    #Monthly sales trends
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_sales=df.groupby('Month')['TotalPrice'].sum()

    plt.figure()
    monthly_sales.plot()
    plt.title('Monthly Sales Trends')
    plt.savefig("outputs?monthly_sales.png")

    #Identify high-value customers
    customers_revenue = df.groupby('CustomerID')['TotalPrice'].sum()
    threshold = customers_revenue.quantile(0.8)

    high_value = customers_revenue[customers_revenue > threshold]

    print(f"Top 20% customers count: {len(high_value)}")
    print(f"Revenue contribution by top customers: {high_value.sum():.2f}")