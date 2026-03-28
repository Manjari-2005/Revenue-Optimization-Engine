import pandas as pd
import sqlite3

df = pd.read_csv('company_sales_data.csv')

conn = sqlite3.connect(':memory:')
df.to_sql('sales', conn, index=False)

queries = {
    "Revenue by Category": """
        SELECT Category, ROUND(SUM(Final_Price * Units_Sold), 2) AS Total_Revenue
        FROM sales GROUP BY Category ORDER BY Total_Revenue DESC
    """,
    "Discount Impact": """
        SELECT Discount_Percent, ROUND(AVG(Units_Sold), 2) AS Avg_Units_Sold
        FROM sales GROUP BY Discount_Percent ORDER BY Discount_Percent
    """,
    "Best Customer Segment": """
        SELECT Customer_Segment, ROUND(SUM(Final_Price * Units_Sold), 2) AS Total_Revenue
        FROM sales GROUP BY Customer_Segment ORDER BY Total_Revenue DESC
    """
}

for title, query in queries.items():
    print(f"\n--- {title} ---")
    print(pd.read_sql_query(query, conn))

conn.close()