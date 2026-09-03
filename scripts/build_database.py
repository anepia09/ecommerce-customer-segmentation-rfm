import sqlite3
import pandas as pd

df = pd.read_csv('data/cleaned_data.csv')

conn = sqlite3.connect('data/retail.db')

df.to_sql('transactions', conn, if_exists='replace', index=False)

print("Database created: data/retail.db")
print("Table 'transactions' has", len(df), "rows")

conn.close()
