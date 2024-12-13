import csv
from io import StringIO
from uuid import uuid4
from datetime import datetime
from data.transactions import Transaction
from data.categories import Category
from data.users import User
from services.exception import NotFoundServiceException, ServiceException

def process_csv_file(user_id, file):
    user = User.get_or_none(id=user_id)
    if user is None:
        raise NotFoundServiceException("User not found.")

    try:
        # Decodifica e lê o arquivo CSV
        file_content = file.read().decode('utf-8')
        csv_reader = csv.DictReader(StringIO(file_content))
        transaction_ids = []

        for row in csv_reader:
            category = Category.get_or_none(name=row.get("category"), user=user)
            if category is None:
                raise NotFoundServiceException(f"Category '{row.get('category')}' not found for user.")

            transaction = Transaction.create(
                id=uuid4(),
                user=user,
                category=category,
                type=row.get("type"),
                value=float(row.get("amount")),
                date=datetime.strptime(row.get("date"), "%Y-%m-%d"),
                description=row.get("description", ""),
                is_recurring=row.get("is_recurring", "false").lower() == "true",
            )
            transaction_ids.append(transaction.id)

        return transaction_ids

    except csv.Error as e:
        raise ServiceException(f"Erro ao ler o CSV: {str(e)}")
    except Exception as e:
        raise ServiceException(f"Erro ao processar a transação: {str(e)}")
