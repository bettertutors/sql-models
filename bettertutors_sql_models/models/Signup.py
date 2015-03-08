from datetime import datetime

from peewee import CharField, DateTimeField

from bettertutors_sql_models.base import BaseModel
from bettertutors_sql_models.custom_fields import EmailField


class Signup(BaseModel):
    email = EmailField(primary_key=True, help_text='Email')
    institute = CharField(index=True)
    role = CharField(index=True)
    registered_on = DateTimeField(default=datetime.now)
