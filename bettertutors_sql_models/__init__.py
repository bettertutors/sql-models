from logging.config import fileConfig
from os import path, environ

from playhouse.db_url import connect


fileConfig(path.join(path.dirname(__file__), 'logging.conf'))

# environ.setdefault('RDBMS_URI', 'sqlite://:memory:')


db = connect(environ['RDBMS_URI'])
