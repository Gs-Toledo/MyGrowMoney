from datetime import datetime
from data.transactions import Transaction
from data.categories import Category
from peewee import fn

def check_budget_alert(category_id):

    # Obtém a categoria e o limite de orçamento
    category = Category.get_by_id(category_id)

    current_month = datetime.now().month
    current_year = datetime.now().year

    total_value = (
        Transaction.select(fn.SUM(Transaction.value))
        .where(
            Transaction.category == category &
            Transaction.date.month == current_month &
            Transaction.date.year == current_year
        )
        .scalar()
    )
    
    if total_value is None:
        total_value = 0

    # Definindo o limite de alerta (90% do limite)
    alert_threshold = category.limit * 0.9
    
    # Verifica se o limite foi alcançado ou ultrapassado
    if total_value >= category.limit:
        print(f"Alerta: Você ultrapassou o orçamento da categoria '{category.name}'!")
        return 'over_budget'
    elif total_value >= alert_threshold:
        print(f"Aviso: Você está perto de atingir o orçamento da categoria '{category.name}'.")
        return 'almost_over_budget'


