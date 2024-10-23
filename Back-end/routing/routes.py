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

    @app.route("/refresh", methods=["GET"])
    @jwt_required()
    def refresh_route():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)

        return jsonify(accessToken=access_token)

    @app.route("/me", methods=["GET"])
    @jwt_required()
    def me_route():
        current_user = get_jwt_identity()
        return jsonify(userId=current_user), 200

        
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

        Transaction.create(
            user=user,
            category=Category.get_by_id(category_id),
            value=value,
            date=date,
            description=description,
            is_recurring=is_recurring
        )

        return jsonify(success=True), 200

    @app.route("/transactions/<id>", methods=["DELETE"])
    @jwt_required()
    def delete_transaction(id):
        transaction = Transaction.get_by_id(id)
        transaction.delete_instance()
        return jsonify(success=True), 200

    @app.route("/categories", methods=["POST"])
    @jwt_required()
    def create_category():
        name = request.json.get("name")
        Category.create(name=name)
        return jsonify(success=True), 200

    @app.route("/categories/<id>", methods=["PUT"])
    @jwt_required()
    def update_category(id):
        category = Category.get_by_id(id)
        category.name = request.json.get("name")
        category.save()
        return jsonify(success=True), 200

    @app.route("/categories/<id>", methods=["DELETE"])
    @jwt_required()
    def delete_category(id):
        category = Category.get_by_id(id)
        category.delete_instance()
        return jsonify(success=True), 200

