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

### 7.4.2 Retrieving Data

To retrieve the values saved in the task table from within a Python program, create a Cursor from a database connection. A cursor produces a consistent view of the data, and is the primary means of interacting with a transactional database system like SQLite.

```
# sqlite3_select_tasks.py
import sqlite3

db_filename = "todo.db"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute(
        """
    select id, priority, details, status, deadline from task
    where project = 'pymotw'
    """
    )

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print(
            "{:2d} [{:d}] {:<25} [{:<8}] ({})".format(
                task_id, priority, details, status, deadline
            )
        )
```

Querying is a two step process. First, run the query with the cursor’s execute() method to tell the database engine what data to collect. Then, use fetchall() to retrieve the results. The return value is a sequence of tuples containing the values for the columns included in the select clause of the query.

```
$ python3 sqlite3_select_tasks.py
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [waiting ] (2016-08-22)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
```

The results can be retrieved one at a time with fetchone(), or in fixed-size batches with fetchmany().

```
# sqlite3_select_variations.py
import sqlite3

db_filename = "todo.db"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute(
        """
    select name, description, deadline from project
    where name = 'pymotw'
    """
    )
    name, description, deadline = cursor.fetchone()

    print("Project details for {} ({})\n  due {}".format(description, name, deadline))

    cursor.execute(
        """
    select id, priority, details, status, deadline from task
    where project = 'pymotw' order by deadline
    """
    )

    print("\nNext 5 tasks:")
    for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row
        print(
            "{:2d} [{:d}] {:<25} [{:<8}] ({})".format(
                task_id, priority, details, status, deadline
            )
        )
```

The value passed to fetchmany() is the maximum number of items to return. If fewer items are available, the sequence returned will be smaller than the maximum value.

```
$ python3 sqlite3_select_variations.py
Project details for Python Module of the Week (pymotw)
  due 2016-11-01

Next 5 tasks:
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [waiting ] (2016-08-22)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
```

### 7.4.3 Query Metadata

The DB-API 2.0 specification says that after execute() has been called, the Cursor should set its description attribute to hold information about the data that will be returned by the fetch methods. The API specification say that the description value is a sequence of tuples containing the column name, type, display size, internal size, precision, scale, and a flag that says whether null values are accepted.

```
# sqlite3_cursor_description.py
import sqlite3

db_filename = "todo.db"

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute(
        """
    select * from task where project = 'pymotw'
    """
    )

    print("Task table has these columns:")
    for colinfo in cursor.description:
        print(colinfo)
```

Because sqlite3 does not enforce type or size constraints on data inserted into a database, only the column name value is filled in.

```
$ python3 sqlite3_cursor_description.py
Task table has these columns:
('id', None, None, None, None, None, None)
('priority', None, None, None, None, None, None)
('details', None, None, None, None, None, None)
('status', None, None, None, None, None, None)
('deadline', None, None, None, None, None, None)
('completed_on', None, None, None, None, None, None)
('project', None, None, None, None, None, None)
```

### 7.4.4 Row Objects

By default, the values returned by the fetch methods as “rows” from the database are tuples. The caller is responsible for knowing the order of the columns in the query and extracting individual values from the tuple. When the number of values in a query grows, or the code working with the data is spread out in a library, it is usually easier to work with an object and access values using their column names. That way, the number and order of the tuple contents can change over time as the query is edited, and code depending on the query results is less likely to break.

Connection objects have a row_factory property that allows the calling code to control the type of object created to represent each row in the query result set. sqlite3 also includes a Row class intended to be used as a row factory. Column values can be accessed through Row instances by using the column index or name.

```
# sqlite3_row_factory.py
import sqlite3

db_filename = "todo.db"

with sqlite3.connect(db_filename) as conn:
    # Change the row factory to use Row
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
    select name, description, deadline from project
    where name = 'pymotw'
    """
    )
    name, description, deadline = cursor.fetchone()

    print("Project details for {} ({})\n  due {}".format(description, name, deadline))

    cursor.execute(
        """
    select id, priority, status, deadline, details from task
    where project = 'pymotw' order by deadline
    """
    )

    print("\nNext 5 tasks:")
    for row in cursor.fetchmany(5):
        print(
            "{:2d} [{:d}] {:<25} [{:<8}] ({})".format(
                row["id"],
                row["priority"],
                row["details"],
                row["status"],
                row["deadline"],
            )
        )
```

This version of the sqlite3_select_variations.py example has been re-written using Row instances instead of tuples. The row from the project table is still printed by accessing the column values through position, but the print statement for tasks uses keyword lookup instead, so it does not matter that the order of the columns in the query has been changed.

```
$ python3 sqlite3_row_factory.py
Project details for Python Module of the Week (pymotw)
  due 2016-11-01

Next 5 tasks:
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [waiting ] (2016-08-22)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
```

### 7.4.5 Using Variables with Queries

Using queries defined as literal strings embedded in a program is inflexible. For example, when another project is added to the database the query to show the top five tasks should be updated to work with either project. One way to add more flexibility is to build an SQL statement with the desired query by combining values in Python. However, building a query string in this way is dangerous, and should be avoided. Failing to correctly escape special characters in the variable parts of the query can result in SQL parsing errors, or worse, a class of security vulnerabilities known as SQL-injection attacks, which allow intruders to execute arbitrary SQL statements in the database.

The proper way to use dynamic values with queries is through host variables passed to execute() along with the SQL instruction. A placeholder value in the SQL is replaced with the value of the host variable when the statement is executed. Using host variables instead of inserting arbitrary values into the SQL before it is parsed avoids injection attacks because there is no chance that the untrusted values will affect how the SQL is parsed. SQLite supports two forms for queries with placeholders, positional and named.

#### 7.4.5.1 Positional Parameters

A question mark (?) denotes a positional argument, passed to execute() as a member of a tuple.

```
# sqlite3_argument_positional.py
import sqlite3
import sys

db_filename = "todo.db"
project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
    select id, priority, details, status, deadline from task
    where project = ?
    """

    cursor.execute(query, (project_name,))

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print(
            "{:2d} [{:d}] {:<25} [{:<8}] ({})".format(
                task_id, priority, details, status, deadline
            )
        )
```

The command line argument is passed safely to the query as a positional argument, and there is no chance for bad data to corrupt the database.

```
$ python3 sqlite3_argument_positional.py pymotw
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [waiting ] (2016-08-22)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
```

#### 7.4.5.2 Named Parameters

Use named parameters for more complex queries with a lot of parameters, or where some parameters are repeated multiple times within the query. Named parameters are prefixed with a colon (e.g., :param_name).

```
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
```

Neither positional nor named parameters need to be quoted or escaped, since they are given special treatment by the query parser.

```
$ python3 sqlite3_argument_named.py pymotw
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [waiting ] (2016-08-22)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
```

Query parameters can be used with select, insert, and update statements. They can appear in any part of the query where a literal value is legal.

```
# sqlite3_argument_update.py
import sqlite3
import sys

db_filename = "todo.db"
id = int(sys.argv[1])
status = sys.argv[2]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "update task set status = :status where id = :id"
    cursor.execute(query, {"status": status, "id": id})
```

This update statement uses two named parameters. The id value is used to find the right row to modify, and the status value is written to the table.

```
$ python3 sqlite3_argument_update.py 2 done
$ python3 sqlite3_argument_named.py pymotw
 1 [1] write about select        [done    ] (2016-04-25)
 2 [1] write about random        [done    ] (2016-08-22)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
```

### 7.4.6 Bulk Loading

To apply the same SQL instruction to a large set of data, use executemany(). This is useful for loading data, since it avoids looping over the inputs in Python and lets the underlying library apply loop optimizations. This example program reads a list of tasks from a comma-separated value file using the [csv](https://pymotw.com/3/csv/index.html) module and loads them into the database.

```
# sqlite3_load_csv.py
import csv
import sqlite3
import sys

db_filename = "todo.db"
data_filename = sys.argv[1]

SQL = """
insert into task (details, priority, status, deadline, project)
values (:details, :priority, 'active', :deadline, :project)
"""

with open(data_filename, "rt") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)
```

The sample data file tasks.csv contains:

```
deadline,project,priority,details
2016-11-30,pymotw,2,"finish reviewing markup"
2016-08-20,pymotw,2,"revise chapter intros"
2016-11-01,pymotw,1,"subtitle"
```

Running the program produces:

```
$ python3 sqlite3_load_csv.py tasks.csv
$ python3 sqlite3_argument_named.py pymotw
 1 [1] write about select        [done    ] (2016-04-25)
 5 [2] revise chapter intros     [active  ] (2016-08-20)
 2 [1] write about random        [done    ] (2016-08-22)
 6 [1] subtitle                  [active  ] (2016-11-01)
 4 [2] finish reviewing markup   [active  ] (2016-11-30)
 3 [1] write about sqlite3       [active  ] (2017-07-31)
```

### 7.4.7 Defining New Column Types

SQLite has native support for integer, floating point, and text columns. Data of these types is converted automatically by sqlite3 from Python’s representation to a value that can be stored in the database, and back again, as needed. Integer values are loaded from the database into int or long variables, depending on the size of the value. Text is saved and retrieved as str, unless the text_factory for the Connection has been changed.

Although SQLite only supports a few data types internally, sqlite3 includes facilities for defining custom types to allow a Python application to store any type of data in a column. Conversion for types beyond those supported by default is enabled in the database connection using the detect_types flag. Use PARSE_DECLTYPES if the column was declared using the desired type when the table was defined.

```
# sqlite3_date_types.py
import sqlite3
import sys

db_filename = "todo.db"

sql = "select id, details, deadline from task"


def show_deadline(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    for col in ["id", "details", "deadline"]:
        print("  {:<8}  {!r:<26} {}".format(col, row[col], type(row[col])))
    return


print("Without type detection:")
with sqlite3.connect(db_filename) as conn:
    show_deadline(conn)

print("\nWith type detection:")
with sqlite3.connect(
    db_filename,
    detect_types=sqlite3.PARSE_DECLTYPES,
) as conn:
    show_deadline(conn)
```

sqlite3 provides converters for date and timestamp columns, using the classes date and datetime from the datetime module to represent the values in Python. Both date-related converters are enabled automatically when type-detection is turned on.

```
$ python3 sqlite3_date_types.py
Without type detection:
  id        1                          <class 'int'>
  details   'write about select'       <class 'str'>
  deadline  '2016-04-25'               <class 'str'>

With type detection:
  id        1                          <class 'int'>
  details   'write about select'       <class 'str'>
  deadline  datetime.date(2016, 4, 25) <class 'datetime.date'>
```

Two functions need to be registered to define a new type. The adapter takes the Python object as input and returns a byte string that can be stored in the database. The converter receives the string from the database and returns a Python object. Use register_adapter() to define an adapter function, and register_converter() for a converter function.

```
# sqlite3_custom_type.py
import pickle
import sqlite3

db_filename = "todo.db"


def adapter_func(obj):
    """Convert from in-memory to storage representation."""
    print("adapter_func({})\n".format(obj))
    return pickle.dumps(obj)


def converter_func(data):
    """Convert from storage to in-memory representation."""
    print("converter_func({!r})\n".format(data))
    return pickle.loads(data)


class MyObj:

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "MyObj({!r})".format(self.arg)


# Register the functions for manipulating the type.
sqlite3.register_adapter(MyObj, adapter_func)
sqlite3.register_converter("MyObj", converter_func)

# Create some objects to save.  Use a list of tuples so
# the sequence can be passed directly to executemany().
to_save = [
    (MyObj("this is a value to save"),),
    (MyObj(42),),
]

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    # Create a table with column of type "MyObj"
    conn.execute(
        """
    create table if not exists obj (
        id    integer primary key autoincrement not null,
        data  MyObj
    )
    """
    )
    cursor = conn.cursor()

    # Insert the objects into the database
    cursor.executemany("insert into obj (data) values (?)", to_save)

    # Query the database for the objects just saved
    cursor.execute("select id, data from obj")
    for obj_id, obj in cursor.fetchall():
        print("Retrieved", obj_id, obj)
        print("  with type", type(obj))
        print()
```

This example uses pickle to save an object to a string that can be stored in the database, a useful technique for storing arbitrary objects, but one that does not allow querying based on object attributes. A real object-relational mapper, such as SQLAlchemy, that stores attribute values in their own columns will be more useful for large amounts of data.

```
$ python3 sqlite3_custom_type.py
adapter_func(MyObj('this is a value to save'))

adapter_func(MyObj(42))

converter_func(b'\x80\x04\x95=\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x05MyObj\x94\x93\x94)\x81\x94}\x94\x8c\x03arg\x94\x8c\x17this is a value to save\x94sb.')

converter_func(b'\x80\x04\x95%\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x05MyObj\x94\x93\x94)\x81\x94}\x94\x8c\x03arg\x94K*sb.')

Retrieved 1 MyObj('this is a value to save')
  with type <class '__main__.MyObj'>

Retrieved 2 MyObj(42)
  with type <class '__main__.MyObj'>
```

### 7.4.8 Determining Types for Columns

There are two sources for types information about the data for a query. The original table declaration can be used to identify the type of a real column, as shown earlier. A type specifier can also be included in the select clause of the query itself using the form as "name [type]".

```
# sqlite3_custom_type_column.py
import pickle
import sqlite3

db_filename = "todo.db"


def adapter_func(obj):
    """Convert from in-memory to storage representation."""
    print("adapter_func({})\n".format(obj))
    return pickle.dumps(obj)


def converter_func(data):
    """Convert from storage to in-memory representation."""
    print("converter_func({!r})\n".format(data))
    return pickle.loads(data)


class MyObj:

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return "MyObj({!r})".format(self.arg)


# Register the functions for manipulating the type.
sqlite3.register_adapter(MyObj, adapter_func)
sqlite3.register_converter("MyObj", converter_func)

# Create some objects to save.  Use a list of tuples so we
# can pass this sequence directly to executemany().
to_save = [
    (MyObj("this is a value to save"),),
    (MyObj(42),),
]

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_COLNAMES) as conn:
    # Create a table with column of type "text"
    conn.execute(
        """
    create table if not exists obj2 (
        id    integer primary key autoincrement not null,
        data  text
    )
    """
    )
    cursor = conn.cursor()

    # Insert the objects into the database
    cursor.executemany("insert into obj2 (data) values (?)", to_save)

    # Query the database for the objects just saved,
    # using a type specifier to convert the text
    # to objects.
    cursor.execute(
        'select id, data as "pickle [MyObj]" from obj2',
    )
    for obj_id, obj in cursor.fetchall():
        print("Retrieved", obj_id, obj)
        print("  with type", type(obj))
        print()
```

Use the detect_types flag PARSE_COLNAMES when the type is part of the query instead of the original table definition.

```
$ python3 sqlite3_custom_type_column.py
adapter_func(MyObj('this is a value to save'))

adapter_func(MyObj(42))

converter_func(b'\x80\x04\x95=\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x05MyObj\x94\x93\x94)\x81\x94}\x94\x8c\x03arg\x94\x8c\x17this is a value to save\x94sb.')

converter_func(b'\x80\x04\x95%\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x05MyObj\x94\x93\x94)\x81\x94}\x94\x8c\x03arg\x94K*sb.')

Retrieved 1 MyObj('this is a value to save')
  with type <class '__main__.MyObj'>

Retrieved 2 MyObj(42)
  with type <class '__main__.MyObj'>
```

### 7.4.9 Transactions

One of the key features of relational databases is the use of _transactions_ to maintain a consistent internal state. With transactions enabled, several changes can be made through one connection without effecting any other users until the results are _committed_ and flushed to the actual database.

#### 7.4.9.1 Preserving Changes

Changes to the database, either through insert or update statements, need to be saved by explicitly calling commit(). This requirement gives an application an opportunity to make several related changes together, so they are stored atomically instead of incrementally, and avoids a situation where partial updates are seen by different clients connecting to the database simultaneously.

The effect of calling commit() can be seen with a program that uses several connections to the database. A new row is inserted with the first connection, and then two attempts are made to read it back using separate connections.

```
# sqlite3_transaction_commit.py
import sqlite3

db_filename = "todo.db"


def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute("select name, description from project")
    for name, desc in cursor.fetchall():
        print("  ", name)


with sqlite3.connect(db_filename) as conn1:
    print("Before changes:")
    show_projects(conn1)

    # Insert in one cursor
    cursor1 = conn1.cursor()
    cursor1.execute(
        """
    insert into project (name, description, deadline)
    values ('virtualenvwrapper', 'Virtualenv Extensions',
            '2011-01-01')
    """
    )

    print("\nAfter changes in conn1:")
    show_projects(conn1)

    # Select from another connection, without committing first
    print("\nBefore commit:")
    with sqlite3.connect(db_filename) as conn2:
        show_projects(conn2)

    # Commit then select from another connection
    conn1.commit()
    print("\nAfter commit:")
    with sqlite3.connect(db_filename) as conn3:
        show_projects(conn3)
```

When show_projects() is called before conn1 has been committed, the results depend on which connection is used. Since the change was made through conn1, it sees the altered data. However, conn2 does not. After committing, the new connection conn3 sees the inserted row.

```
$ python3 sqlite3_transaction_commit.py
Before changes:
   pymotw

After changes in conn1:
   pymotw
   virtualenvwrapper

Before commit:
   pymotw

After commit:
   pymotw
   virtualenvwrapper
```