from uuid import uuid4

from services.exception import ServiceException
from data.users import User


def sign_up(name: str, email: str, password: str):
    user_found_by_email = User.get_or_none(email=email)

    if user_found_by_email is not None:
        raise SignUpServiceException("Email is already registered")

    User.create(
        id=uuid4(),
        name=name,
        email=email,
        password=password
    )


class SignUpServiceException(ServiceException):
    pass
