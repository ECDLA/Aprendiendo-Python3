from base import DatabaseManagementSystem
from settings import *
import hashlib
import sqlite3

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
        return hashlib.new(PASSWORD_HASH_ALGORITHM, password.encode('utf-8')).hexdigest()

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
                    query, (None, int(USER_DEFAULT_ANIMATION), int(USER_DEFAULT_FLICKER), self.id)
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

    def set_user_configuration(self, animation: bool, flicker: bool):
        if self.authenticate_user():
            if not (isinstance(animation, bool) and isinstance(flicker, bool)):
                raise Exception('Invalid values, must be boolean values.')

            # Update user settings
            query = 'UPDATE users_configuration SET animation = ?, flicker = ? WHERE user_id = ?'
            DatabaseManagementSystem.run_query(query, (int(animation), int(flicker), self.id))

            return {'animation': animation, 'flicker': flicker}

        else:
            raise UserNotExists(f'User "{ self.username }" does not exist.')
 
    def get_user_configuration(self):
        if self.authenticate_user():
            query = 'SELECT animation, flicker FROM users_configuration WHERE user_id = ?'
            result = DatabaseManagementSystem.run_query(query, (self.id,)).fetchall()[0]

            return {'animation': bool(result[0]), 'flicker': bool(result[1]) }

        else:
            raise UserNotExists(f'User "{ self.username }" does not exist.')
    
if __name__ == '__main__':
    pass