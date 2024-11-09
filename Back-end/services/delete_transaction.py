from data.transactions import Transaction

def delete_transaction(transaction_id):
    transaction = Transaction.get_by_id(transaction_id)

    if transaction is not None:
        transaction.delete_instance()