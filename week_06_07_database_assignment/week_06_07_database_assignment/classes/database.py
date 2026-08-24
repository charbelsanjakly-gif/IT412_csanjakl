"""
database module

Contains the Database class, which wraps the PyMySQL connection code
shown in the "Testing Your Database Environment" lecture into a
reusable class. All SQL statements sent through this class follow the
SELECT / INSERT / UPDATE / DELETE patterns from the SQL Commands
Reference Guide lecture.
"""

import pymysql


class Database:
    """
    Wraps a PyMySQL connection to a MariaDB/MySQL database so the rest
    of the program does not need to deal with connection details or
    cursors directly.
    """

    def __init__(self, host, user, password, db, charset='utf8mb4'):
        """
        Open a connection to the database.

        host -- database server host (e.g. 'localhost')
        user -- database username
        password -- database password
        db -- name of the database to connect to
        charset -- character set to use for the connection
        """
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
            charset=charset,
            cursorclass=pymysql.cursors.DictCursor
        )

    def fetch_all(self, sql, params=None):
        """
        Run a SELECT statement and return every matching row as a
        list of dictionaries (column name -> value).

        sql -- the SQL statement, with %s placeholders for any values
        params -- tuple of values to substitute into the placeholders
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

    def fetch_one(self, sql, params=None):
        """
        Run a SELECT statement and return only the first matching row
        as a dictionary, or None if there were no matches.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchone()

    def execute(self, sql, params=None):
        """
        Run an INSERT, UPDATE, or DELETE statement and commit the
        change. Returns the number of rows affected.

        sql -- the SQL statement, with %s placeholders for any values
        params -- tuple of values to substitute into the placeholders
        """
        with self.connection.cursor() as cursor:
            rows_affected = cursor.execute(sql, params)
            self.connection.commit()
            return rows_affected

    def close(self):
        """Close the database connection."""
        self.connection.close()
