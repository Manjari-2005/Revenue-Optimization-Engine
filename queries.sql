-- 1. Total Revenue by Category
SELECT Category, 
       ROUND(SUM(Final_Price * Units_Sold), 2) AS Total_Revenue
FROM sales
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- 2. Average Discount Impact on Units Sold
SELECT Discount_Percent,
       ROUND(AVG(Units_Sold), 2) AS Avg_Units_Sold,
       ROUND(AVG(Final_Price), 2) AS Avg_Price
FROM sales
GROUP BY Discount_Percent
ORDER BY Discount_Percent;

-- 3. Best Customer Segment by Revenue
SELECT Customer_Segment,
       ROUND(SUM(Final_Price * Units_Sold), 2) AS Total_Revenue,
       COUNT(*) AS Total_Orders
FROM sales
GROUP BY Customer_Segment
ORDER BY Total_Revenue DESC;

-- 4. Monthly Sales Trend
SELECT strftime('%Y-%m', Date) AS Month,
       ROUND(SUM(Final_Price * Units_Sold), 2) AS Monthly_Revenue
FROM sales
GROUP BY Month
ORDER BY Month;