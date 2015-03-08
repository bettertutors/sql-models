from os import environ

from peewee import Model
from playhouse.db_url import connect

db = connect(environ['RDBMS_URI'])


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db
