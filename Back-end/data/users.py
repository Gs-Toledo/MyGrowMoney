from uuid import uuid4
from peewee import Model, CharField, UUIDField
from data.database import database

class User(Model):
    class Meta:
        database = database

    id = UUIDField(primary_key=True)
    name = CharField()
    email = CharField()
    password = CharField()

    def check_password(self, password: str):
        return self.password == password
    
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
        }


User.create_table()
