from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, 
    get_jwt_identity, jwt_required
)

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

    @app.route("/users/<user_id>/transactions", methods=["GET"])
    @jwt_required()
    def get_user_route(user_id):
        return jsonify(userId=user_id), 200
