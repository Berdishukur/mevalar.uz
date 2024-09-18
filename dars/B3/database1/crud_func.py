import sqlite3
from  contextlib import closing
database_path="sample-database (8).db"
def get_connection(database_path):
    return closing(sqlite3.connect(database_path))

def get_employee(database_path,employee_id):
    with get_connection(database_path) as connection:
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id=?",(employee_id,))
        return cursor.fetchone()
emp=get_employee(database_path,101)
print(emp)





