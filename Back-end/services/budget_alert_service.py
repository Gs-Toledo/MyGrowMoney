from datetime import datetime
from data.transactions import Transaction
from peewee import fn


def check_budget_alert(categoria):

    if categoria is None:
        print(f"Erro: Categoria {categoria} não encontrada.")
        return "category_not_found"

    current_month = datetime.now().month
    current_year = datetime.now().year

    # Calcula o valor total das transações do mês e ano atuais
    total_value = (
        Transaction.select(fn.SUM(Transaction.value))
        .where(
            (Transaction.category == categoria)
            & (fn.strftime("%m", Transaction.date) == f"{current_month:02}")
            & (fn.strftime("%Y", Transaction.date) == str(current_year))
        )
        .scalar()
    )

    if total_value is None:
        total_value = 0

    # Definindo o limite de alerta (90% do limite)
    alert_threshold = categoria.limit * 0.9

    # Verifica se o limite foi alcançado ou ultrapassado
    if total_value >= categoria.limit:
        print(
            f"Alerta: Você ultrapassou o orçamento da categoria '{categoria.name}'!" # noqa
        )  # noqa
        return "over"
    elif total_value >= alert_threshold:
        print(
            f"Aviso: Você está perto de atingir o orçamento da categoria '{categoria.name}'."  # noqa
        )
        return "almost"
    return "far"
