# sqlite3_argument_named.py
import sqlite3
import sys

db_filename = "todo.db"
project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = :project_name
    order by deadline, priority
    """

    cursor.execute(query, {"project_name": project_name})

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print(
            "{:2d} [{:d}] {:<25} [{:<8}] ({})".format(
                task_id, priority, details, status, deadline
            )
        )
