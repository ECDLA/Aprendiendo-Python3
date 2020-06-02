from .base import DatabaseManagementSystem
from .settings import *
import hashlib
import curses

# Decorator beta version ->
def user_authentication_required(func):

    def wrapper(obj, user_obj, *args, **kwargs):
        if not user_obj.is_authenticated:
            if not user_obj.authenticate_user():
                raise Exception('Authentication failed')

        return func(obj, user_obj, *args, **kwargs)

    return wrapper

class UserConfigurationTableManagement:
    column_name = None
    _query_result = None

    def __getattribute__(self, name):
        if name in ['__get__', '__set__']:
            if super().__getattribute__('column_name') is None:
                raise Exception('Attribute "column_name" must not be None.')

        return super().__getattribute__(name)

    @user_authentication_required
    def __get__(self, obj, type):
        if self._query_result is None:
            self._query_result = DatabaseManagementSystem.run_query(
                f'SELECT {self.column_name} FROM users_configuration WHERE user_id = ?', 
                [obj.id]

            ).fetchone()[0]
            
        return self._query_result

    @user_authentication_required
    def __set__(self, obj, value):
        DatabaseManagementSystem.run_query(
            f'UPDATE users_configuration SET {self.column_name} = ? WHERE user_id = ?', 
            [value, obj.id]
        )
        
        self._query_result = None

    def __delete__(self, obj): pass

class AnimationColumnManagement(UserConfigurationTableManagement):
    column_name = 'animation'
    VALID_VALUES = (0, 12)

    def __set__(self, obj, value):
        if value not in self.VALID_VALUES or isinstance(value, bool):
            raise Exception('Invalid value.')

        super().__set__(obj, value)

class FlickerColumnManagement(UserConfigurationTableManagement):
    column_name = 'flicker'
    VALID_VALUES = ('A_BLINK', 'A_STANDOUT')

    def __get__(self, obj, type):
        return getattr(curses, super().__get__(obj, type))

    def __set__(self, obj, value):
        if value not in self.VALID_VALUES:
            raise Exception('Invalid value.')

        super().__set__(obj, value)

class User:

    animation_config = AnimationColumnManagement()
    flicker_config = FlickerColumnManagement()

    def __init__(self, username: str, password: str):
        self.id = None
        self.username = username
        self._password = password
        self.is_authenticated = False

    def __str__(self):
        return self.username

    @classmethod
    def generate_password_hash(cls, password: str):
        return hashlib.new(PASSWORD_HASH_ALGORITHM, password.encode('utf-8')).hexdigest()

    def create_user(self):
        """ Returns True if the user was created successfully, and False if it is the opposite. """
        
        if self.is_authenticated: return None

        try:
            password_hash = self.generate_password_hash(self._password)

            DatabaseManagementSystem.run_query(
                'INSERT INTO users VALUES(?, ?, ?)',  (None, self.username, password_hash)
            )

            # Set attributes
            self.id = DatabaseManagementSystem.run_query(
                'SELECT id FROM users WHERE username = ?', (self.username,)

            ).fetchone()[0]

            self._password = password_hash
            self.is_authenticated = True

            # Create user settigs
            DatabaseManagementSystem.run_query(
                'INSERT INTO users_configuration VALUES(?, ?, ? ,?)', 
                (None, USER_DEFAULT_ANIMATION, USER_DEFAULT_FLICKER, self.id)
            )

            return True

        except sqlite3.IntegrityError:
            return False

    def authenticate_user(self):
        """ Returns True if the user authenticated successfully, and False if the opposite """

        if self.is_authenticated: return True

        password_hash = self.generate_password_hash(self._password)

        result = DatabaseManagementSystem.run_query(
            'SELECT id FROM users WHERE username = ? AND password = ?', 
            (self.username, password_hash)
            
        ).fetchone()

        if not result: return False

        # Set attributes
        self.id = result[0]
        self._password = password_hash
        self.is_authenticated = True

        return True

if __name__ == '__main__':
    pass