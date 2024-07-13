 ## 🟧 install `sqlite3 libsqlite3-dev`


<br>

- this module didnt work the first time i downloaded the **python3.8.18**


<br>


<br>


In Python, **sqlite3** and **dbapi2** are often referenced together because  <u>sqlite3 is a module that implements the Python Database **API** Specification v2.0 (**DB-API 2.0**) for **SQLite** databases</u>.


The terms **sqlite3.dbapi2**, **sqlite3**, and **libsqlite3**-dev relate to SQLite, a popular embedded database engine used within Python and other programming languages. Here’s a breakdown of each term:
<br>

```javascript

  // ✋ sqlite3.dbapi2
  File "<string>", line 1, in <module>
  File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/sqlite3/__init__.py", line 23, in <module>
    from sqlite3.dbapi2 import *
  File "/home/mycomputer/.pyenv/versions/3.8.18/lib/python3.8/sqlite3/dbapi2.py", line 27, in <module>
    from _sqlite3 import *
ModuleNotFoundError: No module named '_sqlite3'
WARNING: The Python sqlite3 extension was not compiled. Missing the SQLite3 lib?
Traceback (most recent call last):



```



<br>

### sqlite3:

- This is the standard Python library module for working with SQLite databases. It provides an interface to interact with SQLite databases using SQL queries. You import it in your Python scripts like this:  `import sqlite3`


In Python, `sqlite3` (**without** **.dbapi2**) specifically refers to the module within the Python standard library that allows you to work with SQLite databases.

It provides functions and classes to interact with SQLite databases, such as creating connections, executing SQL queries, and managing transactions.

<br>
<br>


**DB-API 2.0 (dbapi2):** This is a standard interface for relational database access in Python. The Python Software Foundation defines this API specification, which allows Python programs to interact with databases in a consistent manner across different database systems.

>**SQLite** implements this DB-API 2.0 standard, meaning that when you use sqlite3 module functions and classes, you are actually using DB-API 2.0-compliant methods.

- This ensures that the code written for SQLite using sqlite3 can be easily adapted to work with other databases supported by Python (like MySQL, PostgreSQL) by simply changing the module used (e.g., mysql.connector, psycopg2).

 <br>