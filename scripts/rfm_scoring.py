import pandas as pd

rfm = pd.read_csv('data/rfm_raw.csv')

# Score Recency: LOWER recency (bought recently) = HIGHER score
# So we reverse the order (labels 5,4,3,2,1 instead of 1,2,3,4,5)
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])

# Score Frequency and Monetary: HIGHER value = HIGHER score
# rank(method='first') handles ties/duplicate values safely
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])

# Combine into a single RFM score string, e.g. "555", "111"
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

# Convert score columns to int for averaging
rfm['R_Score'] = rfm['R_Score'].astype(int)
rfm['F_Score'] = rfm['F_Score'].astype(int)
rfm['M_Score'] = rfm['M_Score'].astype(int)

# Assign segment labels based on R and F scores (simple, interpretable rule set)
def assign_segment(row):
    r, f, m = row['R_Score'], row['F_Score'], row['M_Score']
    if r >= 4 and f >= 4 and m >= 4:
        return 'Champions'
    elif r >= 3 and f >= 3:
        return 'Loyal Customers'
    elif r <= 2 and f >= 4:
        return 'At Risk'
    elif r >= 4 and f <= 2:
        return 'New Customers'
    elif r <= 2 and f <= 2 and m <= 2:
        return 'Lost'
    else:
        return 'Needs Attention'

rfm['Segment'] = rfm.apply(assign_segment, axis=1)

print("Segment counts:")
print(rfm['Segment'].value_counts())

print("\nSample rows:")
print(rfm.head(10))

rfm.to_csv('data/rfm_segmented.csv', index=False)
print("\nSaved rfm_segmented.csv")
