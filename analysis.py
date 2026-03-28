import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Load your company data
df = pd.read_csv('company_sales_data.csv')

# 2. Visualize Price Sensitivity per Category
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
g = sns.lmplot(data=df, x='Final_Price', y='Units_Sold', col='Category', 
               hue='Category', col_wrap=2, sharex=False)
g.fig.suptitle('Price Sensitivity Analysis: Sales vs Price', y=1.05)

# 3. Save the chart for your GitHub
plt.savefig('pricing_analysis_chart.png')
plt.show()

# 4. Calculate the 'Sensitivity Score'
print("\n--- ANALYTICAL RESULTS ---")
for cat in df['Category'].unique():
    subset = df[df['Category'] == cat]
    slope, intercept, r_val, p_val, std_err = linregress(subset['Final_Price'], subset['Units_Sold'])
    print(f"Category: {cat:15} | Sensitivity: {abs(slope):.4f}")
    # 5. Demand Elasticity + Revenue Impact
print("\n--- REVENUE IMPACT OF DISCOUNTS ---")
df['Revenue'] = df['Final_Price'] * df['Units_Sold']

revenue_by_discount = df.groupby('Discount_Percent')['Revenue'].mean().reset_index()
print(revenue_by_discount)

# 6. Best performing category
print("\n--- TOTAL REVENUE BY CATEGORY ---")
print(df.groupby('Category')['Revenue'].sum().sort_values(ascending=False))

# 7. Recommendations
print("\n--- RECOMMENDATIONS ---")
print("1. Books: Highly price-sensitive → Use bundle deals")
print("2. Electronics: Low sensitivity → Premium pricing works")
print("3. Clothing: Medium sensitivity → Seasonal discounts effective")
print("4. Home & Kitchen: Medium → Bundling recommended")

# 8. Save summary to CSV
summary = df.groupby('Category').agg(
    Avg_Price=('Final_Price', 'mean'),
    Avg_Units_Sold=('Units_Sold', 'mean'),
    Total_Revenue=('Revenue', 'sum')
).reset_index()

summary.to_csv('pricing_summary.csv', index=False)
print("\nSummary saved to pricing_summary.csv!")