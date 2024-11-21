from datetime import datetime
from peewee import fn
from data.transactions import Transaction


def get_monthly_summary(user_id):
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Total de receitas do mês
    receitas = (Transaction
                .select(fn.SUM(Transaction.value))
                .where(
                    (Transaction.user == user_id) &
                    (Transaction.type == "receita") &
                    (fn.strftime("%m", Transaction.date) == f"{current_month:02}") &
                    (fn.strftime("%Y", Transaction.date) == str(current_year))
                )
                .scalar()) or 0

    # Total de despesas do mês
    despesas = (Transaction
                .select(fn.SUM(Transaction.value))
                .where(
                    (Transaction.user == user_id) &
                    (Transaction.type == "despesa") &
                    (fn.strftime("%m", Transaction.date) == f"{current_month:02}") &
                    (fn.strftime("%Y", Transaction.date) == str(current_year))
                )
                .scalar()) or 0

    # Saldo do mês
    saldo = receitas - despesas

    return {
        "receitas": receitas,
        "despesas": despesas,
        "saldo": saldo
    }
