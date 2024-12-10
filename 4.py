import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create the 'emp' table (Employee details)
cursor.execute('''
CREATE TABLE IF NOT EXISTS emp (
    empno INTEGER PRIMARY KEY,
    deptno INTEGER,
    name TEXT,
    age INTEGER
)
''')

# Create the 'dept' table (Department details)
cursor.execute('''
CREATE TABLE IF NOT EXISTS dept (
    deptno INTEGER PRIMARY KEY,
    name TEXT
)
''')

# Insert data into the 'emp' table
cursor.executemany('''
INSERT INTO emp (empno, deptno, name, age)
VALUES (?, ?, ?, ?)
''', [
    (1, 1, 'Smith', 30),
    (2, 1, 'Adam', 25),
    (3, 2, 'Yamamoto', 31),
    (4, 3, 'Lan', 38),
    (5, 3, 'Mike', 33)
])

# Insert data into the 'dept' table
cursor.executemany('''
INSERT INTO dept (deptno, name)
VALUES (?, ?)
''', [
    (1, 'IT'),
    (2, 'Admin'),
    (3, 'Sales')
])

# Commit the changes
conn.commit()

# SQL Query to join the 'emp' and 'dept' tables
cursor.execute('''
SELECT emp.empno, emp.name AS emp_name, emp.age, dept.name AS dept_name
FROM emp
INNER JOIN dept ON emp.deptno = dept.deptno
''')

# Fetch the results and print
print("Employees with their department:")
for row in cursor.fetchall():
    print(f"Empno: {row[0]}, Emp Name: {row[1]}, Age: {row[2]}, Dept Name: {row[3]}")

# SQL Query for a specific view (emp_no, name, and dept name)
cursor.execute('''
SELECT emp.empno, emp.name AS emp_name, dept.name AS dept_name
FROM emp
INNER JOIN dept ON emp.deptno = dept.deptno
''')

# Fetch and display
print("\nEmployees and their department names:")
for row in cursor.fetchall():
    print(f"Empno: {row[0]}, Emp Name: {row[1]}, Dept Name: {row[2]}")

# Closing the connection
conn.close()
