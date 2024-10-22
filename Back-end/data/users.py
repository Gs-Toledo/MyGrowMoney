from uuid import uuid4
from peewee import Model, CharField, UUIDField
from data.database import database


class User(Model):
    class Meta:
        database = database

    id = UUIDField(default=uuid4(), primary_key=True)
    name = CharField()
    email = CharField()
    password = CharField()

    def check_password(self, password: str):
        return self.password == password


User.create_table()
