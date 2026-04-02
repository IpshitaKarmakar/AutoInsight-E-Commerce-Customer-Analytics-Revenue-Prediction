import pandas as pd
def preprocess_transactions(df):
    print(f"\n Staring preprocessing..")

    df.columns = df.columns.str.strip().str.replace(" ", " ")

    print("Columns after cleaning:",df.columns)

    #rename columns
    df = df.rename(columns={
        'Invoice': 'InvoiceNo',
        'Price': 'UnitPrice'
    })

    #Check required columns exist
    required_cols = ['CustomerID', 'Quantity', 'UnitPrice', 'InvoiceDate']

    for col in required_cols:
        if col not in df.columns:
            print(f"Error: {col} not found in dataset")
            return df
        
    #Remove missing customer IDs
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]   

    #remove duplicates
    df = df.drop_duplicates()

    #convert date column
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    #create business feature 
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    print(f"Data cleaned. Remaining records: {df.shape[0]}")

    return df
     


