import os.path

# DATABASE
# ------------------------------------------------------------------------------

DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

# USER
# ------------------------------------------------------------------------------

PASSWORD_HASH_ALGORITHM = 'md5'

# USER CONFIGURATION
# ------------------------------------------------------------------------------

# Warning!: integer values only!, valid values: 0, 12
USER_DEFAULT_ANIMATION = 12

# Warning: string value only!, valid values: 'A_BLINK', 'A_STANDOUT'
USER_DEFAULT_FLICKER = 'A_BLINK'
    