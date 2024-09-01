CREATE TABLE employee(
  employee_id varchar PRIMARY KEY,
  employee_name varchar,
  employee_job varchar,
  employee_salary REAL
);
INSERT INTO employee(employee_id,employee_name,employee_job,employee_salary)
  VALUES
('0321','Josh','project manager','103,000'),
('0332','Maanas','jr developer','83,000'),
('0343','Ekta','business analyst','87,000'),
('0335','Nikhil','Sr developer','128,000');