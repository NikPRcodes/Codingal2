SELECT department_id, SUM(salary) 
FROM department
GROUP BY department_id;