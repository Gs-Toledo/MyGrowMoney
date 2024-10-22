from uuid import uuid4
from peewee import Model, UUIDField
from data.database import database


class Category(Model):
    class Meta:
        database = database

    id = UUIDField(default=uuid4(), primary_key=True)


Category.create_table()
