SQL - Introduction
===================

## General

* What’s a database

A SQL database is a collection of tables
that stores a specific set of structured data.

* [What’s a relational database](https://phoenixnap.com/kb/what-is-a-relational-database)

A relational database is a type of database that focuses on the relation between
stored data elements. It allows users to establish links between
different sets of data within the database and
use these links to manage and reference related data.
In a relational database, each row in the table is a record with a unique ID
called the key.

  * It's a database
  * Is a collection of data
  * The data are organized by tables, records and columns
  * a table containing only one object representation (Unique ID)

* What does SQL stand for(https://dsstream.com/what-is-a-relational-database/)

SQL (Structured Query Language)

* What’s MySQL

The relational model introduced SQL (Structured Query Language),
which is the main language used to access and modify data in databases.
The Basics of Relational Database Implementation.
Databases have different implementations.
They also differ in the version of SQL they support.

(1)MySQL is one of many RDBMS (Relational Database Management System) software options.
RDBMS and MySQL are often thought to be the same because of MySQL's popularity.

**Fun Fact**
>> A few big web applications like;
>> Facebook, Twitter, YouTube, Google, and Yahoo!
>> all use MySQL for data storage purposes.

Even though it was initially created for limited usage


ref:

(1):[What's MySQL](https://www.hostinger.com/tutorials/what-is-mysql)

* How to create a database in MySQL

#The CREATE DATABASE statement is used to create a new SQL database.

Syntax looks like this...

```
CREATE DATABASE databasename;

'''example'''

CREATE DATABASE testDB;
```

* What does `DDL` and `DML` stand for

|:DDL:|:DML|
|-----|----|
|**Data Definition Language**| **Data Manipulation Language**|
|are used to build and modify the structure of your tables and other objects in the database.|used to work with the data in tables. When you are connected to most multi-user databases (whether in a client program or by a connection from a Web page script)|


* How to `CREATE` or `ALTER` a table

#Create
The statement 'CREATE' can be used to specify a table, or constraints key constraints.
```
CREATE TABLE <table name> (
<attribute name 1> <data type 1>,
...
<attribute name n> <data type n>);

```
#Alter
The Alter table is frequently used to specify primary and foreign key contraints, and
make onther modifications to the table structure.
```
ALTER TABLE <table name>
ADD CONSTRAINT <constraint name> PRIMARY KEY (<attribute list>);
```

###[SELECT](https://www.w3schools.com/mysql/mysql_select.asp)

To explain how to `SELECT` data from a table, we will use the
`**SELECT** * FROM table_name` command to select all the columns of a given table.

for example; here we are selecting all the columns/data of the employee table.

```
mysql> SELECT * FROM employee;
```

### [How to `INSERT`, `UPDATE` or `DELETE` data](https://codedec.com/tutorials/how-to-select-insert-delete-update-and-delete-data-in-mysql/)

**INSERT**

```
INSERT INTO table_name(field1, field 2, field 3, fieldN)

VALUES

(value1, value2 , value3, valuen);


CREATE TABLE emp (
emp_id INT NOT NULL,
emp_Firstname VARCHAR (100),
emp_Surname VARCHAR(100),
PRIMARY KEY (emp_id)
);
INSERT INTO emp (emp_id,emp_Firstname,emp_Surname) VALUES (2, 'dick', 'cena');

```

**UPDATE**

```
UPDATE table_name SET field1=new-value1, field2=new-value2
[Where clause]
```

```
UPDATE emp
SET emp_Firstname ='Jimmy'
WHERE emp_id =2;

```

**DELETE**

```
DELETE FROM Table_name
WHERE
(condition applied);
Example:
DELETE FROM emp WHERE emp_id =2;
```

* What are `subqueries`

A Subquery or Inner query or a Nested query is a query within another SQL query and embedded within the WHERE clause. A subquery is used to return data that will be used in the main query as a condition to further restrict the data to be retrieved.
Also a subquary is a query that is nested inside a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery.

* How to use MySQL functions

MySQL has many built-in functions/stored program and can be used to
pass parameters into and then return a value. wheather string, numeric, date, and some advanced functions in MySQL.

Resources
==========

**Read or watch:**

* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
* [Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
* [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* [Raw SQL in a Rails project](https://web.archive.org/web/20181124213655/http://gmile.me:80/raw-sql-in-a-rails-project/)
* [SELECT example](https://dyclassroom.com/mysql/mysql-select-from-table)
* [Subquary](https://docs.microsoft.com/en-us/sql/relational-databases/performance/subqueries)
  * [moreover](https://duckduckgo.com/?q=What+are+subqueries&t=brave&ia=web)
* [MySQL functions](https://www.techonthenet.com/mysql/functions.php)
* [What is a relational Database](https://www.oracle.com/database/what-is-a-relational-database/)
  * [moreover](https://duckduckgo.com/?q=what%27s+a+relational+database&t=brave&ia=web)

