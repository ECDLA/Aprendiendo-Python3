from .base import DatabaseManagementSystem
from .settings import *
import hashlib
import sqlite3

# Decorator beta version ->
def user_authentication_required(func):

    def wrapper(obj, user_obj, *args, **kwargs):
        if not user_obj.is_authenticated:
            if not user_obj.authenticate_user():
                raise Exception('Authentication failed')

        return func(obj, user_obj, *args, **kwargs)

    return wrapper


class ColumnManagement():

    def __init__(self, column_name): self.column_name = column_name

    @user_authentication_required
    def __get__(self, obj, type):
        return bool(
            DatabaseManagementSystem.run_query(
                f'SELECT {self.column_name} FROM users_configuration WHERE user_id = ?', 
                [obj.id]

            ).fetchone()[0]
        )

    @user_authentication_required
    def __set__(self, obj, value):
        if isinstance(value, bool):
            DatabaseManagementSystem.run_query(
                f'UPDATE users_configuration SET {self.column_name} = ? WHERE user_id = ?', 
                [int(value), obj.id]
            )
        else:
            raise Exception('Must be a boolean value')

    def __delete__(self, obj): 
        pass

class User():

    animation_config = ColumnManagement('animation')
    flicker_config = ColumnManagement('flicker')

    ATTRS_REQUIRING_AUTHENTICATION = (
        'animation_config',
        'flicker_config',
    )

    def __init__(self, username: str, password: str):
        self.id = None
        self.username = username
        self._password = password
        self.is_authenticated = False

    def __str__(self):
        return self.username

    # def __getattribute__(self, name):
    #     if name in super().__getattribute__('ATTRS_REQUIRING_AUTHENTICATION'):
    #         if not super().__getattribute__('authenticate_user')():
    #             raise Exception('')

    #     return super().__getattribute__(name)

    @classmethod
    def generate_password_hash(cls, password: str):
        return hashlib.new(PASSWORD_HASH_ALGORITHM, password.encode('utf-8')).hexdigest()

    def create_user(self):
        """ Returns True if the user was created successfully, and False if it is the opposite. """
        
        if not self.is_authenticated:
            try:
                query = 'INSERT INTO users VALUES(?, ?, ?)'

                password_hash = self.generate_password_hash(self._password)
                DatabaseManagementSystem.run_query(query, (None, self.username, password_hash))

                query = 'SELECT id FROM users WHERE username = ?'
                result = DatabaseManagementSystem.run_query(query, (self.username,)).fetchall()

                # Set attributes
                self.id = result[0][0]
                self._password = password_hash
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

            password_hash = self.generate_password_hash(self._password)
            result = DatabaseManagementSystem.run_query(
                query, (self.username, password_hash)
                
            ).fetchall()

            if result:
                # Set attributes
                self.id = result[0][0]
                self._password = password_hash
                self.is_authenticated = True

                return True

            return False
        
        else:
            return True

if __name__ == '__main__':
    pass