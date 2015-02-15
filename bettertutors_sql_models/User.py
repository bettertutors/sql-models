from datetime import datetime

from peewee import Model, CharField, DateTimeField

from __init__ import db


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class User(BaseModel):
    email = CharField(primary_key=True, help_text='Email')
    institute = CharField(index=True)
    role = CharField(index=True)
    registered_on = DateTimeField(default=datetime.now)
