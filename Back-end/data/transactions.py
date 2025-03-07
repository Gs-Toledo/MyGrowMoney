from enum import Enum
from uuid import uuid4
from peewee import Model, UUIDField, ForeignKeyField, FloatField, DateField, TextField, BooleanField
from datetime import datetime

from data.database import database
from data.users import User
from data.categories import Category

class TransactionType(Enum): 
    RECEITA = 'receita'  
    DESPESA = 'despesa'

class Transaction(Model):
    class Meta:
        database = database

    id = UUIDField(primary_key=True)
    user = ForeignKeyField(User, backref='transactions')
    type = TextField(choices=[(tag, tag.value) for tag in TransactionType]) #Tipo da transação
    category = ForeignKeyField(Category, backref='transactions')
    value = FloatField()  # Valor da transação
    date = DateField()  # Data da transação
    description = TextField()  # Descrição da transação
    is_recurring = BooleanField(default=False)  # Transação recorrente

Transaction.create_table()

def generate_recurring_transactions():
    today = datetime.date.today()
    recurring_transactions = Transaction.select().where(Transaction.is_recurring == True)

    for transaction in recurring_transactions:
        # Se passou 30 dias desde a última transação, crie uma nova
        if (today - transaction.date).days >= 30:
            Transaction.create(
                user=transaction.user,
                category=transaction.category,
                type=transaction.type,
                value=transaction.value,
                date=today,
                description=transaction.description,
                is_recurring=True
            )