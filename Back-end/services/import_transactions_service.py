import csv
from io import StringIO
from uuid import uuid4
from datetime import datetime
from data.transactions import Transaction
from data.categories import Category
from data.users import User
from services.exception import NotFoundServiceException, ServiceException
from services.create_category import create_category
from features import is_import_transactions_enabled

def process_csv_file(user_id, file):
    if not is_import_transactions_enabled():
        raise ServiceException("Import transactions feature is disabled")

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
                # Cria a categoria e obtém o ID
                category_id = create_category(user.id, row.get("category"), limit=500)
                # Busca a instância da categoria criada
                category = Category.get(id=category_id)

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
