FRUITS_EXPORT (Schema):
seller_info (table):
- seller_id
- fruit_id
- fruit_weight (tons)
consumption_info (table):
- fruit_id
- seller_id
- client_id
- quantity_purchased_fruit (tons)
Write a PostgreSQL query to find the following:
2.1. How many tons worth of fruit does an average seller have?
2.2. How many sellers have at least one client who purchased their fruit?

2.1.
SELECT 
    AVG(SumWeight) AS AvgWght 
FROM 
    (
    SELECT 
	SUM(fruit_weight) AS SumWeight
    FROM seller_info
    GROUP BY seller_id
    ) AS avg_result;

2.2.
SELECT 
    COUNT(DISTINCT(seller_id))
FROM consumption_info
WHERE quantity_purchased_fruit (tons) > 0;
