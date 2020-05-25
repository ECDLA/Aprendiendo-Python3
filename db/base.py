from .settings import DATABASE_NAME
import sqlite3
import os.path

class DatabaseManagementSystem():

    @classmethod
    def initilize_tables(cls):
        """ Create tables in the database """

        try:
            query = """
                CREATE TABLE users(
                    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                    "username" TEXT UNIQUE,
                    "password" TEXT
                )
            """

            cls.run_query(query)

            query = """
                CREATE TABLE users_configuration(
                    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                    "animation" INTEGER,
                    "flicker" TEXT,
                    "user_id" INTEGER NOT NULL UNIQUE REFERENCES users("id")
                )
            """

            cls.run_query(query)

        except sqlite3.OperationalError:
            pass

    @classmethod
    def run_query(cls, query: str, parameters = ()):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, parameters)
            connection.commit()

        return result