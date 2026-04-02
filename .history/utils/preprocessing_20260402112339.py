import pandas as pd
def preprocess_transactions(df):
    print(f"\n Staring preprocessing..")

    #drop rows where customer id is missing 
    df=df.dropna(subset=['CustomerID'])

    #remove invalid transactions 
    df=df[(df['Quantity']>0) & (df['UnitPrice']>0)]

    #remove duplicate values
    df=df.drop_duplicates()

    #convert data column
    df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])

    #create total transaction values
    df['TotalPrice']=df['Quantity']*df['UnitPrice']

    print(f"Data cleaned. Remaining records: {df.shape[0]}")
    
    return df