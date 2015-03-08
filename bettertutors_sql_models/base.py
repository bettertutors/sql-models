from peewee import Model

from __init__ import db


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db
