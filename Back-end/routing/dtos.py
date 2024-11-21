def to_transaction_dto(transaction):
    return {
        "id": transaction.id,
        "value": transaction.value,
        "description": transaction.description,
        "date": transaction.date,
        "type": transaction.type,
        "category": to_category_dto(transaction.category),
        "is_recurring": transaction.is_recurring,
    }


def to_transactions_dto(transactions):
    transactions_dto = []

    for transaction in transactions:
        transactions_dto.append(to_transaction_dto(transaction))

    return transactions_dto


def to_category_dto(category):
    return {"user": category.user.id ,"id": category.id, "name": category.name, "limit": category.limit}


def to_categories_dto(categories):
    categories_dto = []

    for category in categories:
        categories_dto.append(to_category_dto(category))

    return categories_dto
