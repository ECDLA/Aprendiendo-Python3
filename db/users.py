from base import DatabaseManagementSystem
import hashlib

HASH_ALGORITHM = 'md5'

class User(DatabaseManagementSystem):

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def create_user(self):
        """
        Returns True if the user was created successfully, and False if it is the opposite.
        Retorna True si el usuario se creo con exito, y False si es lo contrario.
        """
        
        try:
            query = 'INSERT INTO users VALUES(?, ?, ?)'

            password_hash = self.generate_password_hash(self.__password)
            self.run_query(query, (None, self.username, password_hash))

            self.__password = password_hash

            return True

        except sqlite3.IntegrityError:
            return False

    @classmethod
    def generate_password_hash(cls, password):
        return hashlib.new(HASH_ALGORITHM, password.encode('utf-8')).hexdigest()

    def authenticate_user(self):
        """
        Returns True if the user authenticated successfully, and False if the opposite
        Retorna True si el usuario se autentico con exito, y False si es lo contrario.
        """

        query = 'SELECT * FROM users WHERE username = ? AND password = ?'

        password_hash = self.generate_password_hash(self.__password)
        result = self.run_query(query, (self.username, password_hash))

        self.__password = password_hash

        return True if result.fetchall() else False

if __name__ == '__main__':
    User('lcteen', 'jcteen-2004').create_user()