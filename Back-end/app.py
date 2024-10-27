from flask import Flask, jsonify
from flask_cors import CORS

from services.exception import ServiceException
from services.sign_up import SignUpServiceException
from routing.routes import register_routes

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "83559534b5a4dc267054fcbb19abaa21d5922e7e14f7ffba442d74b80f861caf"  # noqa


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, SignUpServiceException):
        return jsonify(success=False, message=str(e)), 400

    if isinstance(e, ServiceException):
        return jsonify(success=False, message=str(e)), 500

    # now you're handling non-HTTP exceptions only
    return jsonify(success=False, message="Internal Server Error: " + str(e)), 500 # noqa


register_routes(app)
