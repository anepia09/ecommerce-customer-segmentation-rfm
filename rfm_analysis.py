import pandas as pd

# Load the cleaned data from Step 3
df = pd.read_csv('data/cleaned_data.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Reference date: since this is historical data, we treat
# the day after the last transaction as "today"
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
print("Snapshot date used for Recency:", snapshot_date)

# Group by customer and calculate R, F, M
rfm = df.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'Invoice': 'nunique',                                      # Frequency
    'Revenue': 'sum'                                           # Monetary
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\nRFM table preview:")
print(rfm.head())
print("\nRFM summary stats:")
print(rfm.describe())

# Save intermediate result
rfm.to_csv('data/rfm_raw.csv')
print("\nSaved rfm_raw.csv")