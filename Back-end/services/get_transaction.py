from data.transactions import Transaction

def get_transaction(id):
    return Transaction.get_by_id(id)