from logging.config import fileConfig
from os import path, environ

from playhouse.db_url import connect

from models.Signup import Signup

fileConfig(path.join(path.dirname(__file__), 'logging.conf'))

# environ.setdefault('RDBMS_URI', 'sqlite://:memory:')

db = connect(environ['RDBMS_URI'])
db.create_tables([Signup], safe=True)  # Not sure if it's good to have this line in the __init__...
