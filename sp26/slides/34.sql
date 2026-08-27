.mode box

-- Simple group by example
select category, count(*) as total, min(ordering), max(ordering)
from principals group by category;

-- Evaluation order

-- Buggy implementation
-- select year from titles 
-- where avg(runtime) > 120 
-- group by year;

select year from titles 
group by year having avg(runtime) > 120;

-- Actors who have played more than 15 different characters
select nconst, count(*) as total
from principals 
where category = "actor" 
group by nconst 
having count(*) > 15;

-- with actor names
select name, count(*) as total 
from principals join names on principals.nconst=names.nconst 
where category = "actor" 
group by names.nconst 
having total > 15;

-- Remakes 
select title, min(year) as first, max(year) as second 
from titles 
group by title 
having count(*) > 1;

-- Getting the actor, averageRating
select names.name, ratings.averageRating 
from ratings join names join principals 
on ratings.tconst = principals.tconst and names.nconst = principals.nconst 
order by averageRating asc limit 7;

-- Getting the actor, averageRating across all movies weighted by numVotes
select names.name, sum(ratings.averageRating * ratings.numVotes) / sum(ratings.numVotes)
from ratings join names join principals 
on ratings.tconst = principals.tconst and names.nconst = principals.nconst 
group by names.nconst
order by averageRating desc limit 7;