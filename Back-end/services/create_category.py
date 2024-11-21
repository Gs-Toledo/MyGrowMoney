from uuid import uuid4

from data.categories import Category
from data.users import User
from services.exception import NotFoundServiceException

def create_category(user_id, name, limit):
    user = User.get_or_none(id=user_id)

    if user is None:
        raise NotFoundServiceException("User was not found")
    
    category = Category.create(
        user=user,  # Referência ao objeto User
        id=uuid4(),
        name=name,
        limit=limit or 0.0
    )

    return category.id
