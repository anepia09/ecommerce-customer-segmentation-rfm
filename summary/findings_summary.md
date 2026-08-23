# Findings & Recommendations

## Summary

This analysis segmented 5,878 customers from an online UK retailer using RFM (Recency, Frequency, Monetary) analysis, based on transaction data from December 2009 to December 2011. The goal was to identify which customer segments contribute most to revenue and which segments represent the greatest risk or opportunity going forward.

## Key Findings

### 1. Revenue is concentrated in a small segment

Champions make up 22% of the customer base but account for approximately 68% of total revenue (£12M of £17.7M). Loyal Customers are the largest segment by headcount (1,403 customers) but contribute far less revenue than Champions, indicating that customer count alone is a poor proxy for customer value.

### 2. At Risk and Lost segments represent a large share of the UK customer base

Of the roughly 5,350 UK customers, 336 are classified as At Risk and 1,192 as Lost — together about 29% of the UK base. These are customers who previously purchased regularly but have not returned recently. Historically valuable customers going quiet represents a recoverable revenue opportunity if approached with the right timing and offer.

### 3. Smaller international markets show signs of bulk/reseller buying behavior

EIRE and the Netherlands generate high revenue per customer (£155,357 and £25,192 average, respectively) despite having very few customers (4 and 22). This is a large enough gap from the UK average (£2,752 per customer) to suggest these markets are not typical retail buyers, and may include wholesale or resale activity. This would need to be confirmed with the business before drawing further conclusions.

## Recommendations

**1. Prioritize win-back campaigns for the At Risk segment before they become Lost.**
At Risk customers have high historical Frequency and Monetary scores but low Recency — they were previously valuable and are still reachable. A time-limited win-back offer targeted specifically at this segment is likely to have a better return than a blanket campaign, since these customers have already demonstrated willingness to spend.

**2. Reduce marketing spend directed at the Lost segment.**
Lost customers score low across Recency, Frequency, and Monetary. Continuing to spend acquisition or retention budget on this segment is unlikely to be efficient. Budget currently allocated here could be reallocated toward the At Risk segment (Recommendation 1) or toward acquiring new Champions-like customers.

**3. Investigate the EIRE and Netherlands markets before treating them as standard retail segments.**
Given the unusually high revenue per customer in these markets, I'd recommend confirming with the business whether these are wholesale/B2B accounts. If so, they should be analyzed and reported separately from retail customers, since mixing them into blended averages distorts metrics like average order value and can lead to misleading conclusions about "typical" customer behavior.

## Limitations & Next Steps

- This dataset is historical (2009-2011) and does not reflect current customer behavior; in a live setting, this analysis would be re-run on a rolling basis (e.g. monthly).
- RFM segments describe past behavior but do not predict future churn probability. With more time or data, a logistic regression or survival analysis model could estimate churn risk more precisely than Recency alone.
- The dataset does not include marketing channel or campaign data, so segment performance could not be broken down by acquisition source. Country was used as a proxy dimension instead.
- No CAC (Customer Acquisition Cost) data was available, so revenue-based recommendations above are directional, not a full ROI calculation.
