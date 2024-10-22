from flask import request, jsonify
from functools import wraps
from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import Length


# Validate a Flask Request using a Marshmallow Schema
def schema(schema_class):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            schema = schema_class()
            json = request.get_json()

            try:
                schema.load(json)
            except ValidationError as err:
                return jsonify(success=False, errors=err.messages), 400

            return f(*args, **kwargs)

        return decorated_function
    return decorator


class SignInSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=Length(min=3))


class SignUpSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=Length(min=3))
