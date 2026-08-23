import pandas as pd

# Load cleaned transaction data and the segmented RFM data
df = pd.read_csv('data/cleaned_data.csv')
rfm = pd.read_csv('data/rfm_segmented.csv')

# the MOST FREQUENT country per customer as their "home" country
customer_country = (
    df.groupby('Customer ID')['Country']
    .agg(lambda x: x.value_counts().index[0])
    .reset_index()
)
customer_country.columns = ['Customer ID', 'Country']

# Merge country info into the RFM table
rfm_with_country = rfm.merge(customer_country, on='Customer ID', how='left')

# Revenue and customer count by country
country_summary = rfm_with_country.groupby('Country').agg(
    total_revenue=('Monetary', 'sum'),
    customer_count=('Customer ID', 'nunique'),
    avg_monetary=('Monetary', 'mean')
).sort_values('total_revenue', ascending=False)

print("TOP 10 COUNTRIES BY REVENUE:")
print(country_summary.head(10))

# Segment distribution by country (top 5 countries only, for readability)
top_countries = country_summary.head(5).index.tolist()
segment_by_country = (
    rfm_with_country[rfm_with_country['Country'].isin(top_countries)]
    .groupby(['Country', 'Segment'])
    .size()
    .unstack(fill_value=0)
)

print("\nSEGMENT DISTRIBUTION (TOP 5 COUNTRIES):")
print(segment_by_country)

rfm_with_country.to_csv('data/rfm_final.csv', index=False)
print("\nSaved rfm_final.csv (this is what we'll load into Tableau/Power BI)")
