import pandas as pd

# Raw data
df = pd.read_csv('data/online_retail_II.csv')

print("BEFORE CLEANING:")
print("Total rows:", len(df))
print("Rows with missing Customer ID:", df['Customer ID'].isna().sum())

# Rows with missing Customer ID
df = df.dropna(subset=['Customer ID'])

# Cancelled invoices (Invoice starting with 'C')
cancelled_mask = df['Invoice'].astype(str).str.startswith('C')
print("Cancelled invoice rows:", cancelled_mask.sum())
df = df[~cancelled_mask]

# Rows with non-positive Quantity or Price
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

# Revenue column (Quantity x Price)
df['Revenue'] = df['Quantity'] * df['Price']

# Convert InvoiceDate to proper datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

print("\nAFTER CLEANING:")
print("Total rows:", len(df))
print("Unique customers:", df['Customer ID'].nunique())
print("Date range:", df['InvoiceDate'].min(), "to", df['InvoiceDate'].max())

df.to_csv('data/cleaned_data.csv', index=False)
print("\nSaved cleaned_data.csv")
