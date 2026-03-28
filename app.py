import streamlit as st
import pandas as pd
import plotly.express as px

# Set Page Config for a professional look
st.set_page_config(page_title="Pricing Strategy Dashboard", layout="wide")

st.title("🚀 Executive Pricing & Revenue Intelligence")
st.markdown("---")

df = pd.read_csv('company_sales_data.csv')

# 1. Top Level Metrics (The KPI Row)
col1, col2, col3 = st.columns(3)
total_revenue = (df['Final_Price'] * df['Units_Sold']).sum()
avg_discount = df['Discount_Percent'].mean() * 100
total_units = df['Units_Sold'].sum()

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Avg Discount %", f"{avg_discount:.1f}%")
col3.metric("Units Sold", f"{total_units:,}")

st.markdown("---")

# 2. Interactive Analysis
st.subheader("Category Performance Analysis")
category = st.selectbox("Select Product Category", df['Category'].unique())

# Filter data based on selection
subset = df[df['Category'] == category]

# 3. Dynamic Price Sensitivity Chart
fig = px.scatter(subset, x="Final_Price", y="Units_Sold", 
                 trendline="ols", 
                 color="Customer_Segment",
                 title=f"Demand Elasticity: {category}",
                 labels={"Final_Price": "Price ($)", "Units_Sold": "Quantity Sold"})

st.plotly_chart(fig, width='stretch')

st.info(f"💡 Strategy Insight: The downward slope indicates how sensitive {category} is to price. Use the legend to see how segments (Standard vs. Premium) react differently.")
st.sidebar.header("📊 Price Simulator")
price_change = st.sidebar.slider("Simulated Price Change (%)", -30, 30, 0)

# Calculate simulated values
# New Price = Current Price * (1 + change)
# New Volume = Current Volume + (Sensitivity * Price Change) 
# Note: Sensitivity is negative, so price up = volume down
sensitivity = abs(subset['Units_Sold'].corr(subset['Final_Price']) * (subset['Units_Sold'].std() / subset['Final_Price'].std()))

simulated_price = subset['Final_Price'].mean() * (1 + price_change/100)
volume_impact = -(sensitivity * (simulated_price - subset['Final_Price'].mean()))
simulated_volume = max(0, subset['Units_Sold'].mean() + volume_impact)

# Display Results
st.subheader("🔮 Predictive Simulation")
sc1, sc2 = st.columns(2)
sc1.metric("Predicted New Price", f"${simulated_price:.2f}", f"{price_change}%")
sc2.metric("Predicted Units/Day", f"{simulated_volume:.1f}", f"{volume_impact:.1f}")

# Revenue Comparison
old_rev = subset['Final_Price'].mean() * subset['Units_Sold'].mean()
new_rev = simulated_price * simulated_volume
rev_delta = new_rev - old_rev

st.write(f"### Projected Revenue Impact: **${rev_delta:,.2f}** per transaction")
st.subheader("📅 Seasonality Trends")
# Group by Day of Week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
seasonal_df = df.groupby('Day_of_Week')['Units_Sold'].mean().reindex(day_order)

st.line_chart(seasonal_df)
st.caption("Insight: Notice the 'Weekend Spike' in demand, which suggests higher price tolerance on Saturdays.")
# Add an "About" section in the sidebar
with st.sidebar:
    st.markdown("---")
    st.header("📌 Project Documentation")
    st.info("""
    This tool analyzes **Price Elasticity of Demand** using a dataset of 2,000+ transactions. 
    - **Models:** Linear Regression
    - **Insights:** Seasonal demand spikes & segment-wise sensitivity.
    """)
    st.success("Developer: Manjari Kamley")

# Add a Data Preview at the very bottom
with st.expander("👀 View Raw Transactional Data"):
    st.dataframe(subset.head(20), width='stretch')
    # ---  SEASONALITY ANALYSIS ---
st.markdown("---")
st.subheader("📅 Demand Seasonality Analysis")

# 1. Create a clean order for the days of the week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 2. Group data by Day of Week and calculate average sales
# Note: This requires you to have run the updated generate_real_data.py first!
seasonal_data = df.groupby('Day_of_Week')['Units_Sold'].mean().reindex(day_order)

# 3. Display the Line Chart
st.line_chart(seasonal_data)

st.caption("🔍 **Strategic Insight:** This trend highlights peak demand periods. In this dataset, the 'Weekend Spike' suggests that customers are less price-sensitive on Saturdays and Sundays, providing an opportunity for premium pricing.")