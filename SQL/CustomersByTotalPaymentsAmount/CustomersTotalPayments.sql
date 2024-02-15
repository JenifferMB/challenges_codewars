-- Replace with your query (in pure SQL)

Select
    c.customer_id,
    c.email,
    Count(p.payment_id) as payments_count,
    Cast(Sum(p.amount) as float) as total_amount
    
From customer c
  Join payment p on c.customer_id = p.customer_id

Group by
    c.customer_id, c.email
Order by
    total_amount Desc
Limit 10