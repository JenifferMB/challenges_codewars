-- Create your SELECT statement here

Select 
    p.id,
    p.name,
    t.people_id,
    Count(t.id) as toy_count

From people p 
    Join toys t on p.id = t.people_id

Group by
    p.id, p.name, t.people_id