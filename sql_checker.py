
import sqlite3


def _make_database():
    """Create isolated sample data for every check."""
    db = sqlite3.connect(":memory:")
    db.executescript("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary REAL,
            department_id INTEGER
        );

        CREATE TABLE departments (
            department_id INTEGER PRIMARY KEY,
            department_name TEXT
        );

        INSERT INTO departments VALUES
            (1, 'IT'), (2, 'HR'), (3, 'Finance');

        INSERT INTO employees
            (id, name, department, salary, department_id)
        VALUES
            (1, 'Ana', 'IT', 60000, 1),
            (2, 'Ben', 'HR', 40000, 2),
            (3, 'Alex', 'IT', 70000, 1),
            (4, 'Devi', 'Finance', 55000, 3),
            (5, 'Sam', NULL, 30000, NULL),
            (6, 'Mia', 'HR', 65000, 2),
            (7, 'Ravi', 'IT', 35000, 1);
    """)
    return db


def _expected_result(validator, db):
    """Return the expected result for each SELECT quest."""
    queries = {
        "select_employees":
            "SELECT * FROM employees",
        "select_name":
            "SELECT name FROM employees",
        "department_it":
            "SELECT * FROM employees WHERE department = 'IT'",
        "salary_gt":
            "SELECT * FROM employees WHERE salary > 50000",
        "salary_desc":
            "SELECT * FROM employees ORDER BY salary DESC",
        "distinct_department":
            "SELECT DISTINCT department FROM employees",
        "count_employees":
            "SELECT COUNT(*) FROM employees",
        "average_salary":
            "SELECT AVG(salary) FROM employees",
        "group_department":
            "SELECT department, COUNT(*) FROM employees GROUP BY department",
        "having_count":
            "SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 5",
        "name_starts_a":
            "SELECT * FROM employees WHERE name LIKE 'A%'",
        "salary_between":
            "SELECT * FROM employees WHERE salary BETWEEN 30000 AND 60000",
        "department_in":
            "SELECT * FROM employees WHERE department IN ('IT', 'HR')",
        "department_null":
            "SELECT * FROM employees WHERE department IS NULL",
        "inner_join":
            "SELECT e.name, d.department_name FROM employees e INNER JOIN departments d ON e.department_id = d.department_id",
        "left_join":
            "SELECT e.name, d.department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id",
        "case_salary":
            "SELECT name, CASE WHEN salary >= 50000 THEN 'High' ELSE 'Standard' END AS salary_band FROM employees",
        "above_average":
            "SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)",
    }

    if validator not in queries:
        return None

    cursor = db.execute(queries[validator])
    rows = cursor.fetchall()
    columns = tuple(item[0] for item in cursor.description)
    return columns, rows


def check_sql_answer(query, validator):
    """Check SQL against expected results in a fresh in-memory database."""
    if not isinstance(query, str) or not query.strip():
        return {"passed": False, "message": "Enter a SQL query."}

    # Only one statement is permitted.
    if ";" in query.strip().rstrip(";"):
        return {"passed": False, "message": "Submit one SQL statement only."}

    db = _make_database()

    try:
        # The INSERT and UPDATE quests are checked in their own fresh database.
        if validator == "insert_employee":
            db.execute(query)
            row = db.execute("""
                SELECT name, department, salary
                FROM employees
                WHERE name='Ana' AND department='IT' AND salary=45000
            """).fetchone()
            passed = row == ("Ana", "IT", 45000.0)

        elif validator == "update_salary":
            db.execute(query)
            row = db.execute(
                "SELECT salary FROM employees WHERE id=7"
            ).fetchone()
            passed = row == (50000.0,)

        else:
            expected = _expected_result(validator, db)
            if expected is None:
                return {
                    "passed": False,
                    "message": "Unknown SQL quest validator."
                }

            # SELECT-only: reject writes and other statement types.
            statement = query.strip().rstrip(";").lstrip().upper()
            if not statement.startswith("SELECT"):
                return {
                    "passed": False,
                    "message": "This quest requires a SELECT query."
                }

            cursor = db.execute(query)
            actual = (tuple(c[0] for c in cursor.description),
                      cursor.fetchall())

            # Compare rows without relying on row order.
            passed = (
                actual[0] == expected[0]
                and sorted(map(repr, actual[1]))
                == sorted(map(repr, expected[1]))
            )

        return {
            "passed": passed,
            "message": (
                "Correct answer!" if passed
                else "The query ran, but its result is incorrect."
            )
        }

    except sqlite3.Error as error:
        return {"passed": False, "message": f"SQL error: {error}"}

    finally:
        db.close()
