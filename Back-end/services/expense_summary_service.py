from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from peewee import fn
from data.transactions import Transaction
from data.categories import Category

def get_expenses_by_category():

    user_id = get_jwt_identity()
    
    # Consulta o total de despesas por categoria do usuário 
    query = (Transaction
             .select(Category.name, fn.SUM(Transaction.value).alias('total'))
             .join(Category)
             .where(Transaction.user == user_id)  # Filtra pelas transações do usuário autenticado
             .group_by(Category.name))
    
    # Formata o resultado
    expenses_data = [{'category': result.category.name, 'total': result.total} for result in query]
    
    return jsonify(success=True, data=expenses_data)
