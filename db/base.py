import sqlite3
import os.path

DATABASE_NAME = 'db.sqlite3'

class DatabaseManagementSystem():

    @classmethod
    def initilize_tables(cls):
        """ Create tables in the database """

        try:
            query = """
                CREATE TABLE users(
                    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                    "username" VARCHAR(50) UNIQUE,
                    "password" VARCHAR(100)
                )
            """

            cls.run_query(query)

            query = """
                CREATE TABLE users_configuration(
                    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                    "animation" INTEGER,
                    "flicker" INTEGER,
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

if __name__ == "__main__":
    # Inicialisamos la db y las tablas
    DatabaseManagementSystem.initilize_tables()