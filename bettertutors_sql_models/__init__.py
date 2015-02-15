__author__ = 'Samuel Marks'

__version__ = '0.1.0'

from logging.config import fileConfig
from os import path, environ
from operator import add

from peewee import SqliteDatabase
from playhouse.postgres_ext import PostgresqlExtDatabase

fileConfig(path.join(path.dirname(__file__), 'logging.conf'))

environ.setdefault('HEROKU_POSTGRESQL_AMBER', 'postgres://username:password@hostname:PORT/dbname')

username, password, hostname, PORT, dbname = reduce(
    add, reduce(add,
                map(lambda e: map(lambda i: i.split('/'), e),
                    map(lambda elem: elem.split(':'),
                        (lambda e: e[e.find('//') + 2:].split('@'))(
                            environ['HEROKU_POSTGRESQL_AMBER']
                        )))))

db = SqliteDatabase(':memory:') if environ.get('SQLITE') else PostgresqlExtDatabase(dbname, user=username)
