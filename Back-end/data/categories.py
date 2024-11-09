from uuid import uuid4
from peewee import Model, UUIDField, CharField, FloatField
from data.database import database


class Category(Model):
    class Meta:
        database = database

    id = UUIDField(primary_key=True)
    name = CharField()  # Nome da categoria
    limit = FloatField(default=0) # Limite de gastos 


Category.create_table()