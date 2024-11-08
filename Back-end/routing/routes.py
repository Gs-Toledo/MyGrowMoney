from uuid import uuid4

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token,
    get_jwt_identity, jwt_required
)

from data.transactions import Transaction
from data.categories import Category
from data.users import User
from services.sign_up import sign_up
from services.sign_in import sign_in
from routing.schemas import SignInSchema, SignUpSchema, schema
from routing.dtos import to_transaction_dto, to_transactions_dto, to_category_dto, to_categories_dto


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

        user_id = sign_in(email=email, password=password)

        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id)

        return jsonify(
            success=True,
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
    def get_all_transactions():
        transactions = Transaction.select().execute()

        transactions_dto = to_transactions_dto(transactions)

        return jsonify(success=True, transactions=transactions_dto)

    @app.route("/transactions/<id>", methods=["GET"])
    @jwt_required()
    def get_transaction(id):
        transaction = Transaction.get_by_id(id)

        transaction_dto = to_transaction_dto(transaction)

        return jsonify(success=True, transaction=transaction_dto)

    @app.route("/transactions", methods=["POST"])
    @jwt_required()
    def create_transaction():
        user_id = get_jwt_identity()
        user = User.get_by_id(user_id)

        category_id = request.json.get("category_id")
        value = request.json.get("value")
        date = request.json.get("date")
        description = request.json.get("description")
        is_recurring = request.json.get("is_recurring", False)

        category = Category.get_or_none(category_id)        

        if category is None:
            return jsonify(success=False, message="Category was not found"), 400

        transaction = Transaction.create(
            id=uuid4(),
            user=user,
            category=category,
            value=value,
            date=date,
            description=description,
            is_recurring=is_recurring
        )

        return jsonify(success=True, transactionId=transaction.id), 200

    @app.route("/transactions/<id>", methods=["DELETE"])
    @jwt_required()
    def delete_transaction(id):
        transaction = Transaction.get_by_id(id)
        transaction.delete_instance()
        return jsonify(success=True), 200
    
    @app.route("/categories/<id>/transactions", methods=["GET"])
    @jwt_required()
    def get_transactions_by_category(id):

        category_id = request.json.get("category_id")

        try:
            category_id = Category.get_by_id(id)
            transactions = Transaction.select().where(Transaction.category == category_id)
            transactions_dto = [to_transaction_dto(transaction) for transaction in transactions]

            return jsonify(success=True, transactions = transactions_dto), 200

        except Category.DoesNotExist:
            return jsonify(success=False, message="Categoria não encontrada"), 404

    @app.route("/categories/<id>/transactions/total", methods=["GET"])
    @jwt_required()
    def get_amount_by_category(id):    
        try:
            category_id = Category.get_by_id(id)
            limit_category = Category.limit
            total_value = (
                Transaction.select(fn.SUM(Transaction.value)).where(Transaction.category_id == category_id).scalar()
            )

            if total_value is None:
                total_value = 0
                return  jsonify(success=True, total = total_value), 200
            
            if total_value > limit_category:
                return jsonify(success=True, total = total_value, message = "Limite da categoria atingido")
            else:
                return jsonify(success=True, total = total_value, message = "Limite da categoria não atingido")
        except Category.DoesNotExist:
            return jsonify(success=False, message="Categoria não encontrada"), 404
    
    @app.route("/categories/<id>/transactions/limt", methods=["GET"])
    @jwt_required()
    def get_compare_limit_by_category(id):   
        
    

    @app.route("/categories", methods=["GET"])
    @jwt_required()
    def get_all_categories():
        categories_cursor = Category.select().execute()

        categories_dto = to_categories_dto(categories_cursor)

        return jsonify(success=True, categories=categories_dto), 200

    @app.route("/categories/<id>", methods=["GET"])
    @jwt_required()
    def get_category(id):
        category = Category.get_by_id(id)

        category_dto = to_category_dto(category)

        return jsonify(success=True, category=category_dto), 200

    @app.route("/categories", methods=["POST"])
    @jwt_required()
    def create_category():
        name = request.json.get("name")
        limit = request.json.get("limit")

        category = Category.create(
            id=uuid4(),
            name=name
            limit=limit
        )

        return jsonify(success=True, categoryId=category.id), 200

    @app.route("/categories/<id>", methods=["PUT"])
    @jwt_required()
    def update_category(id):
        category = Category.get_by_id(id)
        category.name = request.json.get("name")
        category.limit = request.json.get("limit")
        category.save()
        return jsonify(success=True), 200

    @app.route("/categories/<id>", methods=["DELETE"])
    @jwt_required()
    def delete_category(id):
        category = Category.get_by_id(id)
        category.delete_instance()
        return jsonify(success=True), 200
