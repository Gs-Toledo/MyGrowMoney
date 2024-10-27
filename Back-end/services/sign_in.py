from data.users import User
from services.exception import ServiceException


def sign_in(email: str, password: str):
    user = User.get_or_none(email=email)

    if user is None:
        raise SignInServiceException("Email is not registered")

    if not user.check_password(password):
        raise SignInServiceException("Password does not match")

    return user.id


class SignInServiceException(ServiceException):
    pass
