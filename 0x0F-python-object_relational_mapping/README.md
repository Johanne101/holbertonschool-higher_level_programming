*Python*
Object-relational mapping
===========================
> ***Before you start…***
> Please make sure your MySQL server is in 8.0

-> How to install MySQL 8.0 in Ubuntu 20.04: (link to repo here)
Learning Objectives
--------------------
**Index**

1. Why Python programming is awesome
2. How to connect to a MySQL database from a Python script
3. How to SELECT rows in a MySQL table from a Python script
4. How to INSERT rows in a MySQL table from a Python script
5. What ORM means
6. How to map a Python Class to a MySQL table
7. Using container-on-demand to run MySQL
8. More Info
9. Resources

## Background Context
<p>
In this project, you will link two amazing worlds: Databases and Python!
In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.
In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).
The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

*Without ORM:*
</p>
how to write a script (first you must import mysql db.

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

*With an ORM:*

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

1. Why Python programming is awesome
-------------------------------------

2. How to connect to a MySQL database from a Python script
----------------------------------------------------------

3. How to SELECT rows in a MySQL table from a Python script
------------------------------------------------------------

4. How to INSERT rows in a MySQL table from a Python script
------------------------------------------------------------

5. What ORM means
-----------------

6. How to map a Python Class to a MySQL table
----------------------------------------------

7. Using container-on-demand to run MySQL
------------------------------------------


## Use *“container-on-demand”* to run MySQL

**In the container, credentials are** `root/root`

* Ask for container `Ubuntu 20.04`
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL before playing with it:

```
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```

## More Info

***Comments for your SQL file:***

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install `MySQLdb` module version 2.0.x

<p>
For installing MySQLdb, you need to have MySQL installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://github.com/Johanne101/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/README.md)
</p>

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install `SQLAlchemy` module version 1.4.x

```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

Also, you can have this warning message:

```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)
```

Resources
=========

<p>
***Read or watch:***

* [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
* [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/) (please don’t pay attention to `_mysql`)]
* [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
* [Introduction to SQLAlchemy](https://github.com/PyMySQL/mysqlclient) (*Youtube*)
* [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
* [10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html) (*Article*)
* [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
* [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/) (**Warning:** *This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL*)
* [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
</p>

