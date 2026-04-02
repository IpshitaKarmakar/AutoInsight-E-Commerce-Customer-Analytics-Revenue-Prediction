from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_customer_model(df):
    print("\n Training customer value prediction model...")

    #Aggregate customer-level data
    customer_data=df.groupby('Customer ID').agg({
        'TotalPrice': 'sum',
         'Quantity' : 'sum'
    }).reset_index()

    #create target: high customer level data 
    threshold=customer_data['TotalPrice'].quantile(0.8)
    customer_data['HighValue']=(customer_data['TotalPrice']>threshold).astype(int)

    X=customer_data[['Quantity','TotalPrice']]
    Y=customer_data['HighValue']

    X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

    model=RandomForestClassifier()
    model.fit(X_train,y_train)

    pred=model.predict(X_test)
    acc=accuracy_score(y_test,pred)

    print(f"Model accuracy: {acc:.2f}")
    print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")