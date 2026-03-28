# 📊 Pricing Strategy Analysis

## 🎯 Problem Statement
What should be the optimal pricing strategy to maximize revenue?

## 🛠️ Tools Used
- Python (Pandas, Matplotlib, Seaborn, Scipy)
- SQL (SQLite)
- Excel / Power BI (Dashboard)

## 📁 Project Structure
Pricing-Strategy-Analysis/
├── generate_real_data.py   # Dataset generation
├── analysis.py             # Price sensitivity analysis
├── run_sql.py              # SQL queries
├── queries.sql             # Raw SQL file
├── company_sales_data.csv  # Dataset (2000 records)
├── pricing_summary.csv     # Summary output
└── pricing_analysis_chart.png  # Visualization
## 📈 Key Findings
- **Books** are highly price-sensitive → Bundle deals recommended
- **Electronics** are price-inelastic → Premium pricing works
- **30% discount** gives highest units sold (avg 11.11)
- **Standard segment** drives maximum revenue

## 💡 Recommendations
| Category | Strategy |
|---|---|
| Books | Bundle deals |
| Electronics | Premium pricing |
| Clothing | Seasonal discounts |
| Home & Kitchen | Product bundling |