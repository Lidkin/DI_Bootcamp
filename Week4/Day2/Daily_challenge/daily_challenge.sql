-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- );

-- INSERT INTO FirstTab
-- VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');

-- SELECT * FROM FirstTab;

-- CREATE TABLE SecondTab (
--     id integer 
-- );

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL);

-- SELECT * FROM SecondTab;

-- Q1: 
-- my_answer: 2
-- right_answer: 0 - It will be 0 because we are doing NOT IN in NOTHING
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- Q2:
-- my_ansver: 2 - It will be 2 ( counted: 6 'Sharlee' and 7, 'Krish' and didn't count 'Avtaar' because his id is null )
--right_answer: 2
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
	
-- Q3:
-- my_ansver: 2
--right_answer: 0 - It will be 0 because SELECT id FROM SecondTab return (5, null) and NOT IN can't take id = null 
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
	
-- Q4:
-- my_ansver: 2 - It will be 2 ( counted: 6 'Sharlee' and 7, 'Krish' and didn't count 'Avtaar' because his id is null )
--right_answer: 2	
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )