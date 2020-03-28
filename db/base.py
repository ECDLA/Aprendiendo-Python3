import sqlite3
import os.path

DATABASE_NAME = 'db.sqlite3'

class DatabaseManagementSystem():

    @classmethod
    def initilize_tables(cls):
        """ Create tables in the database """

        if not os.path.exists(DATABASE_NAME):
            query = """
                CREATE TABLE users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(50),
                    password VARCHAR(100),

                    UNIQUE(username)
                )
            """

            cls.run_query(query)

    @classmethod
    def run_query(cls, query, parameters = ()):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, parameters)
            connection.commit()

        return result

if __name__ == "__main__":
    # Inicialisamos la db y las tablas
    DatabaseManagementSystem.initilize_tables()
    