import sqlite3
import pandas as pd

# Load cleaned data
df = pd.read_csv('data/cleaned_data.csv')

# SQLite database file
conn = sqlite3.connect('data/retail.db')

# Dataframe into a SQL table called 'transactions'
df.to_sql('transactions', conn, if_exists='replace', index=False)

print("Database created: data/retail.db")
print("Table 'transactions' has", len(df), "rows")

conn.close()