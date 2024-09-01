-- Select all records from the STUDENT table to verify insertion
SELECT * FROM STUDENT;

-- Query students who are 18 years old and live in Delhi
SELECT * FROM STUDENT WHERE AGE = 18 AND ADDRESS = 'DELHI';

-- Query students who are 18 years old and named RAM
SELECT * FROM STUDENT WHERE AGE = 18 AND NAME = 'RAM';

-- Query students named Ram or Sujit
SELECT * FROM STUDENT WHERE NAME = 'RAM' OR NAME = 'SUJIT';

-- Query students named Ram or aged 20
SELECT * FROM STUDENT WHERE NAME = 'RAM' OR AGE = 20;

-- Query students aged 18 and named Ram or Ramesh
SELECT * FROM STUDENT WHERE AGE = 18 AND (NAME = 'RAM' OR NAME = 'RAMESH');