import pandas as pd
from utils.preprocessing import preprocess_transactions
from utils.analysis import explore_business_transactions
from utils.modeling import train_customer_model

def run_pipeline():
    file_path=input("Enter the CSV path = ")
    -