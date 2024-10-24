from uuid import uuid4
from peewee import Model, UUIDField, CharField
from data.database import database

class Category(Model):
    class Meta:
        database = database

    id = UUIDField(default=uuid4(), primary_key=True)
    name = CharField()  # Nome da categoria


Category.create_table()