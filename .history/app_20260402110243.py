import pandas as pd
from utils.preprocessing import preprocess_transactions
from utils.analysis import explore_business_transactions
from utils.modeling import train_customer_model

def run_pipeline():
    file_path=input("Enter the CSV path = ")

    try:
        df=pd.read_csv(file_path, encoding='ISO-8859-1')
        print(f"\n Dataset loaded successfully with shape: {df.shape}")
    except Exception as e:
        print("File error",e)  
        return  
    
    df=preprocess_transactions(df)
    explore_business_transactions(df)
    train_customer_model(df)
    
if __name__ == "__main__":
    run_pipeline()    