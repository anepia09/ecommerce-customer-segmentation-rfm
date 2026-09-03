import pandas as pd

df = pd.read_csv('data/cleaned_data.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
print("Snapshot date used for Recency:", snapshot_date)


rfm = df.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  
    'Invoice': 'nunique',                                      
    'Revenue': 'sum'                                          
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\nRFM table preview:")
print(rfm.head())
print("\nRFM summary stats:")
print(rfm.describe())

# Save intermediate result
rfm.to_csv('data/rfm_raw.csv')
print("\nSaved rfm_raw.csv")
