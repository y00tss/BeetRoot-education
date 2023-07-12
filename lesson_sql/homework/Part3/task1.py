-- write a query in SQL to display the first name, last name, department number, and department name for each employee
SELECT e.first_name, e.last_name, e.department_id, d.department_name FROM employees AS e, department d WHERE e.department_id = d.department_id;

-- write a query in SQL to display the first and last name, department, city, and state province for each employee
SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province FROM employees AS e, departments as d, locations AS l WHERE e.department_id = d.department_id AND d.location_id = l.location_id;

-- write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT e.first_name, e.last_name, e.department_id, d.department_name FROM employees AS e, department AS d WHERE e.department_id = d.department_id AND (e.department_id = 80 OR e.department_id = 40);

-- write a query in SQL to display all departments including those where does not have any employee
SELECT department_name FROM department;

-- write a query in SQL to display the first name of all employees including the first name of their manager
SELECT e.first_name AS employees, m.first_name AS manager FROM employees AS e, employees AS m WHERE e.manager_id = m.employee_id;

-- write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT j.job_title, first_name || ' ' || last_name AS fullname,j.max_salary - e.salary AS difference FROM employees AS e, jobs AS j WHERE e.job_id = j.job_id;
-- SELECT j.job_title, first_name || ' ' || last_name AS fullname, j.max_salary ,j.max_salary - e.salary AS difference, e.salary FROM employees AS e, jobs AS j WHERE e.job_id = j.job_id; -- for better clarity

-- write a query in SQL to display the job title and the average salary of employees
SELECT j.job_title, AVG(e.salary) AS avg_salary FROM employees AS e, jobs AS j WHERE e.job_id = j.job_id GROUP BY e.department_id ORDER BY avg_salary DESC;

-- write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT first_name || ' ' || last_name AS fullname, salary FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE location_id IN (SELECT location_id FROM locations WHERE city = 'Seattle'));

-- write a query in SQL to display the department name and the number of employees in each department
SELECT d.department_name, COUNT(d.department_id) AS count_dep FROM department AS d, employees AS e WHERE d.department_id = e.department_id GROUP BY d.department_name;