from uuid import uuid4

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)

import logging

from services.budget_alert_service import check_budget_alert
from services.expense_summary_service import get_expenses_by_category

from data.transactions import Transaction
from data.categories import Category
from data.users import User
from services.sign_up import sign_up
from services.sign_in import sign_in

from services.get_transaction import get_transaction
from services.create_transaction import create_transaction
from services.delete_transaction import delete_transaction
from services.get_all_transactions import get_all_transactions
from services.exception import NotFoundServiceException

from services.get_category import get_category
from services.create_category import create_category
from services.update_category import update_category
from services.delete_category import delete_category
from services.get_all_categories import get_all_categories

from services.import_transactions_service import process_csv_file
from services.exception import ServiceException

from services.monthly_summary_service import get_balance_by_month
from services.currency_service import listar_moedas, converter

from routing.schemas import SignInSchema, SignUpSchema, schema
from routing.dtos import (
    to_transaction_dto,
    to_transactions_dto,
    to_category_dto,
    to_categories_dto,
)

def register_routes(app: Flask):
    jwt = JWTManager(app)
    bcrypt = Bcrypt(app)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    @app.route("/sign-in", methods=["POST"])
    @schema(SignInSchema)
    def sign_in_route():
        email = request.json.get("email")
        password = request.json.get("password")

        user = sign_in(email=email, password=password)
        print(user)
        user_id = user.id

        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id)
        userPayload = user.to_dict()

        return jsonify(
            success=True,
            user=userPayload,
            accessToken=access_token,
            refreshToken=refresh_token,
        )

    @app.route("/sign-up", methods=["POST"])
    @schema(SignUpSchema)
    def sign_up_route():
        name = request.json.get("name")
        email = request.json.get("email")
        password = request.json.get("password")

        sign_up(name=name, email=email, password=password)

        return jsonify(success=True), 200

    @app.route("/refresh", methods=["POST"])
    @jwt_required(refresh=True)
    def refresh_route():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)

        return jsonify(accessToken=access_token)

    @app.route("/me", methods=["GET"])
    @jwt_required()
    def me_route():
        current_user = get_jwt_identity()
        return jsonify(userId=current_user), 200

    @app.route("/transactions", methods=["GET"])
    @jwt_required()
    def get_all_transactions_route():
        user_id = get_jwt_identity()
        user = User.get_or_none(id=user_id)
        if user is None:
            return jsonify(success=False, message="User not found"), 404

        transactions = Transaction.select().where(Transaction.user == user)
        transactions_dto = to_transactions_dto(transactions)

        return jsonify(success=True, transactions=transactions_dto)

    @app.route("/transactions/<id>", methods=["GET"])
    @jwt_required()
    def get_transaction_route(id):
        user_id = get_jwt_identity()
        user = User.get_or_none(id=user_id)
        if user is None:
            return jsonify(success=False, message="User not found"), 404

        try:
            transaction = Transaction.get(
                Transaction.id == id, Transaction.user == user
            )
            transaction_dto = to_transaction_dto(transaction)
            return jsonify(success=True, transaction=transaction_dto)
        except Transaction.DoesNotExist:
            return jsonify(success=False, message="Transaction not found"), 404

    # Configuração de logging
    logging.basicConfig(level=logging.DEBUG)

    @app.route("/transactions", methods=["POST"])
    @jwt_required()
    def create_transaction_route():
        user_id = get_jwt_identity()
        user = User.get_or_none(id=user_id)
        if user is None:
            logging.debug("User not found: %s", user_id)
            return jsonify(success=False, message="User not found"), 404

        category_id = request.json.get("categoryId")
        transaction_type = request.json.get("type")
        value = request.json.get("value")
        date = request.json.get("date")
        description = request.json.get("description")
        is_recurring = request.json.get("is_recurring", False)

        category = Category.get_or_none(
            Category.id == category_id, Category.user == user
        )
        if category is None:
            logging.debug(
                "Category not found or does not belong to the user: %s", category_id
            )
            return jsonify(success=False, message="Category not found"), 404

        transaction = Transaction.create(
            id=uuid4(),
            user=user,
            category=category,
            type=transaction_type,
            value=value,
            date=date,
            description=description,
            is_recurring=is_recurring,
        )

        budget_alert = check_budget_alert(category)

        return (
            jsonify(
                success=True, transactionId=transaction.id, budget_alert=budget_alert
            ),
            200,
        )

    @app.route("/transactions/<id>", methods=["DELETE"])
    @jwt_required()
    def delete_transaction_route(id):
        user_id = get_jwt_identity()
        user = User.get_or_none(id=user_id)
        if user is None:
            return jsonify(success=False, message="User not found"), 404

        try:
            transaction = Transaction.get(
                Transaction.id == id, Transaction.user == user
            )
            transaction.delete_instance()
            return jsonify(success=True), 200
        except Transaction.DoesNotExist:
            return jsonify(success=False, message="Transaction not found"), 404
    
    @app.route("/transactions/<id>", methods=["PUT"])
    @jwt_required()
    def update_transaction_route(id):
        user_id = get_jwt_identity()  # Obtém o ID do usuário do token JWT
        user = User.get_or_none(id=user_id)
        if user is None:
            return jsonify(success=False, message="User not found"), 404

        name = request.json.get("name")
        limit = request.json.get("limit")
        transaction_type = request.json.get("type")
        value = request.json.get("value")
        date = request.json.get("date")
        description = request.json.get("description")
        is_recurring = request.json.get("is_recurring", False)

        try:
            # Verifica se a transação pertence ao usuário autenticado
            transaction = Transaction.get(Transaction.id == id, Transaction.user == user_id)
            # Atualiza os campos da transação
            transaction.name = name
            transaction.limit = limit
            transaction.type = transaction_type
            transaction.value = value
            transaction.date = date
            transaction.description = description
            transaction.is_recurring = is_recurring
            transaction.save()

            return jsonify(success=True), 200
        except Transaction.DoesNotExist:
            return jsonify(success=False, message="Transaction not found"), 404
        except Exception as e:
            return jsonify(success=False, message="An error occurred while updating the transaction."), 500


    @app.route("/categories/<id>/transactions", methods=["GET"])
    @jwt_required()
    def get_transactions_by_category(id):
        user_id = get_jwt_identity()
        user = User.get_or_none(id=user_id)
        if user is None:
            return jsonify(success=False, message="User not found"), 404

        try:
            category = Category.get(Category.id == id, Category.user == user)
            transactions = Transaction.select().where(Transaction.category == category)
            transactions_dto = [
                to_transaction_dto(transaction) for transaction in transactions
            ]

            return jsonify(success=True, transactions=transactions_dto), 200
        except Category.DoesNotExist:
            return jsonify(success=False, message="Category not found"), 404

    @app.route("/categories", methods=["GET"])
    @jwt_required()
    def get_all_categories_route():
        user_id = get_jwt_identity()  # Obtém o ID do usuário do token JWT
        user = User.get_or_none(id=user_id)

        if user is None:
            raise NotFoundServiceException("User was not found")

        categories = Category.select().where(Category.user == user)
        categories_dto = to_categories_dto(categories)

        return jsonify(success=True, categories=categories_dto), 200

    @app.route("/categories", methods=["POST"])
    @jwt_required()
    def create_category_route():
        user_id = get_jwt_identity()  # Obtém o ID do usuário do token JWT
        name = request.json.get("name")
        limit = request.json.get("limit")

        try:
            category_id = create_category(user_id, name, limit)
            return jsonify(success=True, categoryId=category_id), 200
        except NotFoundServiceException as e:
            return jsonify(success=False, message=str(e)), 404

    @app.route("/categories/<id>", methods=["GET"])
    @jwt_required()
    def get_category_route(id):
        user_id = get_jwt_identity()  # Obtém o ID do usuário do token JWT

        try:
            category = Category.get(Category.id == id, Category.user == user_id)
            category_dto = to_category_dto(category)

            return jsonify(success=True, category=category_dto), 200
        except Category.DoesNotExist:
            return jsonify(success=False, message="Categoria não encontrada"), 404

    @app.route("/categories/<id>", methods=["PUT"])
    @jwt_required()
    def update_category_route(id):
        user_id = get_jwt_identity()  # Obtém o ID do usuário do token JWT
        name = request.json.get("name")
        limit = request.json.get("limit")

        try:
            category = Category.get(Category.id == id, Category.user == user_id)
            update_category(id, name, limit)
            return jsonify(success=True), 200
        except Category.DoesNotExist:
            return jsonify(success=False, message="Categoria não encontrada"), 404

    @app.route("/categories/<id>", methods=["DELETE"])
    @jwt_required()
    def delete_category_route(id):
        user_id = get_jwt_identity()  # Obtém o ID do usuário do token JWT

        try:
            category = Category.get(Category.id == id, Category.user == user_id)  # noqa
            delete_category(id)
            return jsonify(success=True), 200
        except Category.DoesNotExist:
            return (
                jsonify(success=False, message="Categoria não encontrada"),
                404,
            )  # noqa

    @app.route("/expenses-by-category", methods=["GET"])
    @jwt_required()
    def expenses_by_category_route():
        return get_expenses_by_category()

    @app.route("/monthly-summary", methods=["GET"])
    @jwt_required()
    def monthly_summary_route():
        user_id = get_jwt_identity()

        try:
            # Obtém o resumo mensal
            summary = get_balance_by_month(user_id)

            return jsonify(summary)

        except Exception as e:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": f"Erro ao gerar resumo mensal: {str(e)}",
                    }
                ),
                500,
            )

    @app.route("/import-transactions", methods=["POST"])
    @jwt_required()
    def import_transactions_route():
        user_id = get_jwt_identity()

        # Verifica se o arquivo foi enviado
        file = request.files.get("file")
        if not file or not file.filename.endswith(".csv"):
            return (
                jsonify(
                    success=False,
                    message="Arquivo invalido. Por favor insira um arquivo válido.",
                ),
                400,
            )

        try:
            # Processa o arquivo CSV com o service
            transaction_ids = process_csv_file(user_id, file)
            return (
                jsonify(
                    success=True,
                    message="Transactions importadas com sucesso",
                    transactionIds=transaction_ids,
                ),
                200,
            )

        except ServiceException as e:
            return jsonify(success=False, message=str(e)), 400
        except Exception as e:
            return jsonify(success=False, message=f"Unexpected error: {str(e)}"), 500

    @app.route('/moedas', methods=['GET'])
    def get_moedas():
        try:
            moedas = listar_moedas()
            return jsonify(moedas)
        except Exception as e:
            return jsonify(success=False, message=f"Erro ao obter as moedas: {str(e)}"), 500

    @app.route('/converter', methods=['POST'])
    def post_converter():
        data = request.json
        if not data or 'moeda_origem' not in data or 'moeda_destino' not in data or 'valor' not in data:
            return jsonify(success=False, message="Dados inválidos"), 400

        moeda_origem = data['moeda_origem']
        moeda_destino = data['moeda_destino']
        valor = data['valor']

        try:
            resultado = converter(moeda_origem, moeda_destino, valor)
            return jsonify(resultado)
        except Exception as e:
            return jsonify(success=False, message=f"Erro ao converter as moedas: {str(e)}"), 500
