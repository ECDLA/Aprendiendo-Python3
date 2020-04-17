from base import DatabaseManagementSystem
import hashlib
import sqlite3

# Constants

HASH_ALGORITHM = 'md5'
USER_DEFAULT_COLOR = 'white'
USER_DEFAULT_TEXT_SPEED = 5.0

class UserNotExists(Exception):
    pass

class User():

    def __init__(self, username: str, password: str):
        self.id = None
        self.username = username
        self.__password = password
        self.is_authenticated = False

    def __str__(self):
        return self.username

    @classmethod
    def generate_password_hash(cls, password: str):
        return hashlib.new(HASH_ALGORITHM, password.encode('utf-8')).hexdigest()

    @classmethod
    def get_all_users(cls):
        return DatabaseManagementSystem.run_query('SELECT * FROM users').fetchall()

    def create_user(self):
        """ Returns True if the user was created successfully, and False if it is the opposite. """
        
        if not self.is_authenticated:
            try:
                query = 'INSERT INTO users VALUES(?, ?, ?)'

                password_hash = self.generate_password_hash(self.__password)
                DatabaseManagementSystem.run_query(query, (None, self.username, password_hash))

                query = 'SELECT id FROM users WHERE username = ?'
                result = DatabaseManagementSystem.run_query(query, (self.username,)).fetchall()

                # Set attributes
                self.id = result[0][0]
                self.__password = password_hash
                self.is_authenticated = True

                # Create user settigs
                query = 'INSERT INTO users_configuration VALUES(?, ?, ? ,?)'

                DatabaseManagementSystem.run_query(
                    query, (None, USER_DEFAULT_COLOR, USER_DEFAULT_TEXT_SPEED, self.id)
                )

                return True

            except sqlite3.IntegrityError:
                return False
        else:
            return None

    def authenticate_user(self):
        """ Returns True if the user authenticated successfully, and False if the opposite """

        if not self.is_authenticated:
            query = 'SELECT id FROM users WHERE username = ? AND password = ?'

            password_hash = self.generate_password_hash(self.__password)
            result = DatabaseManagementSystem.run_query(
                query, (self.username, password_hash)
                
            ).fetchall()

            if result:
                # Set attributes
                self.id = result[0][0]
                self.__password = password_hash
                self.is_authenticated = True

                return True

            return False
        
        else:
            return True

    def set_user_configuration(self, color: str, text_speed: float):
        if self.authenticate_user():
            # Update user settings
            query = 'UPDATE users_configuration SET color = ?, text_speed = ? WHERE user_id = ?'
            DatabaseManagementSystem.run_query(query, (color, text_speed, self.id))

            return {'color': color, 'text_speed': text_speed}

        else:
            raise UserNotExists(f'User "{ self.username }" does not exist.')
 
    def get_user_configuration(self):
        if self.authenticate_user():
            query = 'SELECT color, text_speed FROM users_configuration WHERE user_id = ?'
            result = DatabaseManagementSystem.run_query(query, (self.id,)).fetchall()[0]

            return {'color': result[0], 'text_speed': result[1]}

        else:
            raise UserNotExists(f'User "{ self.username }" does not exist.')
    
if __name__ == '__main__':
    pass