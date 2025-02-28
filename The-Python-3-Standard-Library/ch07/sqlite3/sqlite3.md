# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.4 sqlite3 — Embedded Relational Database](https://pymotw.com/3/sqlite3/index.html)

Purpose:	Implements an embedded relational database with SQL support.

The sqlite3 module implements a [Python DB-API 2.0](https://peps.python.org/pep-0249/) compliant interface to SQLite, an in-process relational database. SQLite is designed to be embedded in applications, instead of using a separate database server program such as MySQL, PostgreSQL, or Oracle. It is fast, rigorously tested, and flexible, making it suitable for prototyping and production deployment for some applications.

### 7.4.1 Creating a Database

An SQLite database is stored as a single file on the file system. The library manages access to the file, including locking it to prevent corruption when multiple writers use it. The database is created the first time the file is accessed, but the application is responsible for managing the table definitions, or schema, within the database.

This example looks for the database file before opening it with connect() so it knows when to create the schema for new databases.

```
# sqlite3_createdb.py
import os
import sqlite3

db_filename = "todo.db"

db_is_new = not os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if db_is_new:
    print("Need to create schema")
else:
    print("Database exists, assume schema does, too.")

conn.close()
```

Running the script twice shows that it creates the empty file if it does not exist.

```
$ ls *.db
ls: cannot access '*.db': No such file or directory
$ python3 sqlite3_createdb.py
Need to create schema
$ python3 sqlite3_createdb.py
Database exists, assume schema does, too.
```

After creating the new database file, the next step is to create the schema to define the tables within the database. The remaining examples in this section all use the same database schema with tables for managing tasks. The details of the database schema are presented in the table below and the table below.

**The project Table**

```
Column	    Type	Description
name	    text	Project name
description	text	Long project description
deadline	date	Due date for the entire project
```

**The task Table**
```
Column	        Type	Description
id	            number	Unique task identifier
priority	    integer	Numerical priority, lower is more important
details	        text	Full task details
status	        text	Task status (one of ‘new’, ‘pending’, ‘done’, or ‘canceled’).
deadline	    date	Due date for this task
completed_on	date	When the task was completed.
project	        text	The name of the project for this task.
```

The data definition language (DDL) statements to create the tables are:

```
-- todo_schema.sql

-- Schema for to-do application examples.

-- Projects are high-level activities made up of tasks
create table project (
    name        text primary key,
    description text,
    deadline    date
);

-- Tasks are steps that can be taken to complete a project
create table task (
    id           integer primary key autoincrement not null,
    priority     integer default 1,
    details      text,
    status       text,
    deadline     date,
    completed_on date,
    project      text not null references project(name)
);
```

The executescript() method of the Connection can be used to run the DDL instructions to create the schema.

```
# sqlite3_create_schema.py
import os
import sqlite3

db_filename = "todo.db"
schema_filename = "todo_schema.sql"

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print("Creating schema")
        with open(schema_filename, "rt") as f:
            schema = f.read()
        conn.executescript(schema)

        print("Inserting initial data")

        conn.executescript(
            """
        insert into project (name, description, deadline)
        values ('pymotw', 'Python Module of the Week',
                '2016-11-01');

        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '2016-04-25',
                'pymotw');

        insert into task (details, status, deadline, project)
        values ('write about random', 'waiting', '2016-08-22',
                'pymotw');

        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2017-07-31',
                'pymotw');
        """
        )
    else:
        print("Database exists, assume schema does, too.")
```

After the tables are created, a few insert statements create a sample project and related tasks. The sqlite3 command line program can be used to examine the contents of the database.

```
$ rm -f todo.db
$ python3 sqlite3_create_schema.py
Creating schema
Inserting initial data
$ sqlite3 todo.db 'select * from task'
1|1|write about select|done|2016-04-25||pymotw
2|1|write about random|waiting|2016-08-22||pymotw
3|1|write about sqlite3|active|2017-07-31||pymotw
```