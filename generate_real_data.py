import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Setup parameters
np.random.seed(42)
records = 2000
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books']

# 2. Generate Base Data
data = {
    'Transaction_ID': [f'TRX-{i:04d}' for i in range(records)],
    'Date': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365)) for i in range(records)],
    'Category': np.random.choice(categories, records),
    'Customer_Segment': np.random.choice(['Premium', 'Standard', 'Student'], records, p=[0.2, 0.5, 0.3])
}

df = pd.DataFrame(data)

# --- NEW SEASONALITY LOGIC STARTS HERE ---
# We extract the day name and month to create "Trends"
df['Day_of_Week'] = df['Date'].dt.day_name()
df['Month'] = df['Date'].dt.month
df['Is_Weekend'] = df['Date'].dt.weekday.isin([5, 6]) # 5=Sat, 6=Sun
# --- NEW SEASONALITY LOGIC ENDS HERE ---

# 3. Price Logic
category_price_map = {'Electronics': 800, 'Clothing': 60, 'Home & Kitchen': 150, 'Books': 25}
df['Base_Price'] = df['Category'].map(category_price_map) + np.random.normal(0, 10, records)
df['Discount_Percent'] = np.random.choice([0, 0.1, 0.2, 0.3], records, p=[0.4, 0.3, 0.2, 0.1])
df['Final_Price'] = df['Base_Price'] * (1 - df['Discount_Percent'])

# --- UPDATED UNITS_SOLD LOGIC ---
# We add multipliers: +25% on Weekends and +40% in December (Month 12)
base_units = (np.random.poisson(5, records) + (df['Discount_Percent'] * 20))

# Applying the "Seasonality Multiplier"
df['Units_Sold'] = (
    base_units * np.where(df['Is_Weekend'], 1.25, 1.0) * np.where(df['Month'] == 12, 1.40, 1.0)
).astype(int)

# 4. Save to CSV
df.to_csv('company_sales_data.csv', index=False)
print("✅ Success: 'company_sales_data.csv' updated with Weekend & Holiday spikes!")