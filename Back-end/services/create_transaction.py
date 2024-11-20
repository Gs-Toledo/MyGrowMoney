from enum import Enum
from uuid import uuid4

from data.transactions import Transaction
from data.categories import Category
from data.users import User
from services.exception import NotFoundServiceException

class TransactionType(Enum):
    RECEITA = 'receita'
    DESPESA = 'despesa'

def create_transaction(
    user_id,
    category_id,
    type,  # Adicione o tipo de transação como argumento
    value,
    date,
    description = "",
    is_recurring = False
):
    user = User.get_or_none(id = user_id)

    if user is None:
        raise NotFoundServiceException("User was not found")

    category = Category.get_or_none(id = category_id)

    if category is None:
        raise NotFoundServiceException("Category was not found")

    transaction = Transaction.create(
        id=uuid4(),
        user=user,
        type=type.value,  # Use o valor do enum
        category=category,
        value=value,
        date=date,
        description=description,
        is_recurring=is_recurring
    )

    return transaction.id
