-- departments (dept_no, dept_name)
DROP TABLE IF EXISTS departments CASCADE;
CREATE TABLE departments (
	dept_no VARCHAR(4) PRIMARY KEY,
	dept_name VARCHAR NOT NULL
);

COPY 
	departments (dept_no, dept_name)
FROM 'D:\BootCamp\sql-challenge\data\departments.csv'
DELIMITER ',' CSV HEADER;

SELECT * FROM departments;

-- employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
DROP TABLE IF EXISTS employees CASCADE;
CREATE TABLE employees (
	emp_no INTEGER PRIMARY KEY, 
	birth_date VARCHAR(10) NOT NULL, 
	first_name VARCHAR NOT NULL, 
	last_name VARCHAR NOT NULL, 
	gender VARCHAR(1) NOT NULL, 
	hire_date VARCHAR(10) NOT NULL
);

COPY 
	employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
FROM 'D:\BootCamp\sql-challenge\data\employees.csv'
DELIMITER ',' CSV HEADER;

SELECT * FROM employees;

-- dept_emp (emp_no, dept_no, from_date, to_date)
DROP TABLE IF EXISTS dept_emp CASCADE;
CREATE TABLE dept_emp (
	emp_no INTEGER NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	dept_no VARCHAR(4) NOT NULL,
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
	from_date VARCHAR(10) NOT NULL,
	to_date VARCHAR(10) DEFAULT '9999-01-01',
	PRIMARY KEY (emp_no, dept_no)
);

COPY 
	dept_emp (emp_no, dept_no, from_date, to_date)
FROM 'D:\BootCamp\sql-challenge\data\dept_emp.csv'
DELIMITER ',' CSV HEADER;

SELECT * FROM dept_emp;

-- dept_manager (dept_no, emp_no, from_date, to_date)
DROP TABLE IF EXISTS dept_manager CASCADE;
CREATE TABLE dept_manager (
	dept_no VARCHAR(4) NOT NULL,
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
	emp_no INTEGER NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	from_date VARCHAR(10) NOT NULL,
	to_date VARCHAR(10) DEFAULT '9999-01-01',
	PRIMARY KEY (dept_no, emp_no)
);

COPY 
	dept_manager (dept_no, emp_no, from_date, to_date)
FROM 'D:\BootCamp\sql-challenge\data\dept_manager.csv'
DELIMITER ',' CSV HEADER;

SELECT * FROM dept_manager;

-- salaries (emp_no, salary, from_date, to_date)
DROP TABLE IF EXISTS salaries CASCADE;
CREATE TABLE salaries (
	id SERIAL PRIMARY KEY,
	emp_no INTEGER NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	salary INTEGER NOT NULL,
	from_date VARCHAR(10) NOT NULL,
	to_date VARCHAR(10) DEFAULT '9999-01-01'
);

COPY 
	salaries (emp_no, salary, from_date, to_date)
FROM 'D:\BootCamp\sql-challenge\data\salaries.csv'
DELIMITER ',' CSV HEADER;

SELECT * FROM salaries;

-- titles (emp_no, title, from_date, to_date)
DROP TABLE IF EXISTS titles CASCADE;
CREATE TABLE titles (
	id SERIAL PRIMARY KEY,
	emp_no INTEGER NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	title VARCHAR NOT NULL,
	from_date VARCHAR(10) NOT NULL,
	to_date VARCHAR(10) DEFAULT '9999-01-01'
);

COPY 
	titles (emp_no, title, from_date, to_date)
FROM 'D:\BootCamp\sql-challenge\data\titles.csv'
DELIMITER ',' CSV HEADER;

SELECT * FROM titles;