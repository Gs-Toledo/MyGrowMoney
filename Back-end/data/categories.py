from uuid import uuid4
from peewee import Model, UUIDField, CharField, FloatField, ForeignKeyField
from data.database import database

from data.users import User

class Category(Model):
    class Meta:
        database = database

    user = ForeignKeyField(User, backref='categories')
    id = UUIDField(primary_key=True)
    name = CharField()  # Nome da categoria
    limit = FloatField(default=0) # Limite de gastos 


Category.create_table()