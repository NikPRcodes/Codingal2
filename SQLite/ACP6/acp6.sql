-- Select all records from the nomnom table
SELECT * FROM nomnom;

-- Select distinct neighborhoods from the nomnom table
SELECT DISTINCT NEIGHBOURHOOD FROM nomnom;

-- Select distinct cuisines from the nomnom table
SELECT DISTINCT CUISINE FROM nomnom;

-- Select all records with Chinese cuisine
SELECT * FROM nomnom WHERE CUISINE = 'Chinese';

-- Select all records with a review rating of 4 or higher
SELECT * FROM nomnom WHERE REVIEW >= 4;

-- Select all records with Italian cuisine and $$$ price
SELECT * FROM nomnom WHERE CUISINE = 'Italian' AND PRICE = '$$$';

-- Select all records where the name contains 'Candy'
SELECT * FROM nomnom WHERE NAME LIKE '%Candy%';

-- Select all records where the neighborhood is Midtown, Downtown, or Chinatown
SELECT * FROM nomnom 
WHERE NEIGHBOURHOOD IN ('Midtown', 'Downtown', 'Chinatown');

-- Select the top 4 records ordered by review rating in descending order
SELECT * FROM nomnom ORDER BY REVIEW DESC LIMIT 4;