from flask import *
from flask_bcrypt import *
from flask_jwt_extended import *

from services.sign_up import *
from services.sign_in import *
from routing.schemas import *

def register_routes (app):
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

        userId = sign_in(
            email = email,
            password = password
        )

        access_token = create_access_token(identity=userId)
        refresh_token = create_refresh_token(identity=userId)

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

        sign_up(
            name = name,
            email = email,
            password = password,
        )

        return jsonify(success = True), 200

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
    
