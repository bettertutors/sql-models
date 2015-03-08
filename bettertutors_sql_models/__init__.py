from logging.config import fileConfig
from os import path, environ


from models.Signup import Signup

fileConfig(path.join(path.dirname(__file__), 'logging.conf'))

# environ.setdefault('RDBMS_URI', 'sqlite://:memory:')
