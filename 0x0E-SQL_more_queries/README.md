SQL - More queries
===================

##General

* How to create a new MySQL user

Here is an example making a new user within the MySQL shell:

```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

```

* How to manage privileges for a user to a database or table

<p>
The first thing to do providing a user with access to the information they will need.

```
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';

```

It's even possible to give only read access to a database to a user and more.

* Here is a short list of other common possible permissions that users can enjoy.

|**Permissions**| **User Privileges** |
|:--------------|:--------------:|
|ALL PRIVILEGES| This allows a MySQL user full access to a designated database (or if no database is selected, global access across the system)|
|CREATE | allows them to create new tables or databases|
|DROP| allows them to them to delete tables or databases|
|DELETE| allows them to delete rows from tables|
|INSERT| allows them to insert rows into tables|
|SELECT| allows them to use the SELECT command to read through databases|
|UPDATE| allow them to update table rows|
|GRANT OPTION| allows them to grant or remove other users’ privileges|

</p>

* What’s a [PRIMARY KEY](https://www.mysqltutorial.org/mysql-primary-key/)

<p>
A primary key is a column or a set of columns that uniquely identifies each row in the table.
The primary key follows these rules:
  1. A primary key must contain unique values. If the primary key consists of multiple columns, the combination of values in these columns must be unique.
  2. A primary key column cannot have NULL values. Any attempt to insert or update NULL to primary key columns will result in an error. Note that MySQL implicitly adds a NOT NULL constraint to primary key columns.
  3. A table can have one an only one primary key.


</p>

* What’s a [FOREIGN KEY](https://www.mysqltutorial.org/mysql-foreign-key/)

<p>
A foreign key is a column or group of columns in a table that links to a column or
group of columns in another table.
The foreign key places constraints on data in the related tables,
which allows MySQL to maintain referential integrity.

As an example the following diagram of customers and orders tables from the sample database.
Each customer can have zero or many orders and each order belongs to one customer.

![alt text](https://www.mysqltutorial.org/wp-content/uploads/2019/08/customers-orders.png)

The relationship between customers table and orders table is one-to-many. And this relationship is established by the foreign key in the orders table specified by the customerNumber column.
</p>

* How to use NOT NULL and UNIQUE constraints

<p>
A column with a NOT NULL constraint, cannot have NULL values.

```
mysql> CREATE TABLE People(Id INTEGER, LastName TEXT NOT NULL,
    ->                     FirstName TEXT NOT NULL, City VARCHAR(55));
Query OK, 0 rows affected (0.07 sec)
```

The first SELECT statement is executed OK, the second one fails. The SQL error says, the LastName column may not be null.
  * first row output

```
mysql> INSERT INTO People VALUES(1, 'Hanks', 'Robert', 'New York');
Query OK, 1 row affected (0.00 sec)

```

  * second row output

```
  mysql> INSERT INTO People VALUES(1, NULL, 'Marianne', 'Chicago');
ERROR 1048 (23000): Column 'LastName' cannot be null
```

</p>

* How to retrieve datas from multiple tables in one request

[Joins and Unions](https://stackoverflow.com/questions/12475850/sql-query-return-data-from-multiple-tables/12475851#12475851)
<p>
Selecting multiple tables using JOIN (cross join)
Example of an implicit cross join:

```
SELECT *
FROM employee, department;
```

A SELECT statement begins with the SELECT keyword and is used to retrieve information from MySQL database tables. You must specify the table name to fetch data from—using the FROM keyword—and one or more columns that you want to retrieve from that table.
Retrieving Multiple Columns
using simple SELECT statement, from an element of table.
The values can be retrieved from two columns in the same query by specifying a list of columns
after the SELECT keyword, separating them with a comma.

```
mysql> SELECT name, price
    -> FROM products;
```

</p>

* What are subqueries

<p>
A subquery is a SELECT statement within another statement.
All subquery forms and operations that the SQL standard requires are supported,
as well as a few features that are MySQL-specific.
Notice that this query below returns a single column and a single row.

```
SELECT * FROM table_1 WHERE column1 = (SELECT column1 FROM table_2);
```

</p>

* What are JOIN and UNION

<p>
||**JOIN**|**UNION**|
|:--:|:--:|:-------:|
|Def.|corresponding to a join operation in relational algebra – combines columns from one or more tables into a new table.|Combines the results of two SQL queries into a single table of all matching rows. The two queries must result in the same number of columns and compatible data types in order to unite.|
|**TYPES**|INNER, LEFT, LEFT OUTER, RIGHT OUTER, FULL OUTER, FULL INNER, TOP and CROSS|UNION, INTERSECT, and EXCEPT|

</p>

###What is...?
|DCL||
|:--:|:--:|
|Data ControlLanguage|

Resources
==========

**Read or watch:**

[How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
[How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
[MySQL constraints](https://zetcode.com/mysql/constraints/): ***NOT NULL, UNIQUE***
[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
[Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
[SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
[SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
[SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
[MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
[The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
[MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
[SQL Style Guide](https://www.sqlstyle.guide/)
[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

**Extra resources around relational database model design:**

[Design](https://www.guru99.com/database-design.html)
[Normalization](https://www.guru99.com/database-normalization.html)
[ER Modeling](https://www.guru99.com/er-modeling.html)

