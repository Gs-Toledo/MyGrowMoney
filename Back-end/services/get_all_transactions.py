from data.transactions import Transaction

def get_all_transactions():
    return Transaction.select().execute()