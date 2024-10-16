from services.exception import ServiceException
from data.users import User

def sign_up (name: str, email: str, password: str):
    user_found_by_email = User.get_or_none(email = email)

    if not user_found_by_email is None:
        raise SignUpServiceException("Email is already registered")
    
    User.create(
        name = name,
        email = email,
        password = password
    )

class SignUpServiceException(ServiceException):
    pass