from uuid import uuid4
from peewee import *

from data.database import database 
from data.users import User

class Transaction(Model):
    class Meta:
        database = database

    id = UUIDField(default = uuid4(), primary_key=True)
    user = ForeignKeyField(User, backref='transactions')

Transaction.create_table()