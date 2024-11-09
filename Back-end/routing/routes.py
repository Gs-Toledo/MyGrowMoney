from uuid import uuid4

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token, 
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)

from services.sign_up import sign_up
from services.sign_in import sign_in

from services.get_transaction import get_transaction
from services.create_transaction import create_transaction
from services.delete_transaction import delete_transaction
from services.get_all_transactions import get_all_transactions

from services.get_category import get_category
from services.update_category import update_category
from services.delete_category import delete_category
from services.get_all_categories import get_all_categories

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
    def get_all_transactions_route():
        transactions = get_all_transactions()

        transactions_dto = to_transactions_dto(transactions)

        return jsonify(success=True, transactions=transactions_dto)

    @app.route("/transactions/<id>", methods=["GET"])
    @jwt_required()
    def get_transaction_route(id):
        transaction = get_transaction(id)

        transaction_dto = to_transaction_dto(transaction)

        return jsonify(success=True, transaction=transaction_dto)

    @app.route("/transactions", methods=["POST"])
    @jwt_required()
    def create_transaction_route():
        user_id = get_jwt_identity()

        category_id = request.json.get("category_id")
        value = request.json.get("value")
        date = request.json.get("date")
        description = request.json.get("description")
        is_recurring = request.json.get("is_recurring", False)

        transaction_id = create_transaction(
            user_id = user_id,
            category_id = category_id,
            value = value,
            date = date,
            description = description,
            is_recurring = is_recurring
        )

        return jsonify(success=True, transactionId=transaction_id), 200

    @app.route("/transactions/<id>", methods=["DELETE"])
    @jwt_required()
    def delete_transaction_route(id):
        delete_transaction(transaction_id = id)

        return jsonify(success=True), 200

    @app.route("/categories", methods=["GET"])
    @jwt_required()
    def get_all_categories_route():
        categories = get_all_categories()

        categories_dto = to_categories_dto(categories)

        return jsonify(success=True, categories=categories_dto), 200

    @app.route("/categories/<id>", methods=["GET"])
    @jwt_required()
    def get_category_route(id):
        category = get_category(id)

        category_dto = to_category_dto(category)

        return jsonify(success=True, category=category_dto), 200

    @app.route("/categories", methods=["POST"])
    @jwt_required()
    def create_category():
        name = request.json.get("name")

        category_id = create_category(
            name = name
        )

        return jsonify(success=True, categoryId=category_id), 200

    @app.route("/categories/<id>", methods=["PUT"])
    @jwt_required()
    def update_category_route(id):
        name = request.json.get("name")

        update_category(
            id,
            name,
        )

        return jsonify(success=True), 200

    @app.route("/categories/<id>", methods=["DELETE"])
    @jwt_required()
    def delete_category_route(id):
        delete_category(id)

        return jsonify(success=True), 200
