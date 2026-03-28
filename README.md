# 📊 E-Commerce Pricing Intelligence & Revenue Simulator

## 🎯 Problem Statement
How can a retailer identify the optimal price point to maximize revenue across diverse product categories while accounting for customer sensitivity and seasonal trends?

## 🚀 Live Demo
[Insert your Streamlit Cloud Link here once hosted!]

## 🛠️ Tech Stack
- **Analysis:** Python (Pandas, Scipy for Linear Regression)
- **Visualization:** Streamlit, Plotly, Seaborn
- **Database:** SQL (SQLite) for segmented revenue reporting
- **Automation:** Synthetic Data Engine for 2,000+ transactional records

## 📁 Project Structure
├── app.py                  # Interactive Streamlit Dashboard
├── generate_real_data.py   # Data engine with Seasonality logic
├── analysis.py             # Statistical price sensitivity analysis
├── run_sql.py              # SQL-based customer segment reporting
├── requirements.txt        # Environment dependencies
└── company_sales_data.csv  # Generated transactional dataset

## 📈 Key Findings & Strategy
- **Price Elasticity:** Electronics show low sensitivity (inelastic); Books show high sensitivity.
- **Seasonality:** Demand increases by **~25% on weekends**, suggesting a "Premium Pricing" opportunity during peak leisure hours.
- **Simulation:** The "What-If" model predicts that a 10% price hike in 'Books' could lead to a significant revenue drop, whereas 'Electronics' can sustain a 15% hike with minimal volume loss.

## 💡 Recommendations
| Category | Strategy | Insight |
|---|---|---|
| **Books** | Bundle deals | High sensitivity; volume is key. |
| **Electronics**| Premium pricing | Low sensitivity; protect margins. |
| **Clothing** | Seasonal discounts| Highly influenced by weekend/holiday trends. |
