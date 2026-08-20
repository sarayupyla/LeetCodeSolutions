select Prices.product_id,
ROUND(coalesce(SUM(Prices.price*UnitsSold.units)/SUM(UnitsSold.units),0),2) as average_price
from Prices
left join UnitsSold
on Prices.product_id=UnitsSold.product_id 
and UnitsSold.purchase_date between Prices.start_date and Prices.end_date
group by Prices.product_id;