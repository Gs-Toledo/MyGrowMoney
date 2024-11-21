from datetime import datetime
from peewee import fn
from data.transactions import Transaction

MONTH_NAMES = {
    "01": "Jan", "02": "Fev", "03": "Mar", "04": "Abr", "05": "Mai", "06": "Jun",
    "07": "Jul", "08": "Ago", "09": "Set", "10": "Out", "11": "Nov", "12": "Dez"
}

def get_balance_by_month(user_id):
    # Agrupa as transações por mês e ano
    query = (Transaction
             .select(
                 fn.strftime("%Y-%m", Transaction.date).alias("year_month"),
                 fn.SUM(Transaction.value).filter(Transaction.type == "receita").alias("total_receitas"),
                 fn.SUM(Transaction.value).filter(Transaction.type == "despesa").alias("total_despesas")
             )
             .where(Transaction.user == user_id)
             .group_by(fn.strftime("%Y-%m", Transaction.date))
             .order_by(fn.strftime("%Y-%m", Transaction.date)))

    # Formata os resultados
    result = []
    for row in query.dicts():
        year_month = row["year_month"]
        year, month_number = year_month.split("-")
        month_name = MONTH_NAMES[month_number]

        receitas = row["total_receitas"] or 0
        despesas = row["total_despesas"] or 0
        saldo = receitas - despesas

        result.append({
            "mes": month_name,
            "receitas": receitas,
            "despesas": despesas,
            "saldo": saldo
        })

    return result
