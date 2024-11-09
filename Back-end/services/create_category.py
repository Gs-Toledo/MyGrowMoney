from uuid import uuid4

from data.categories import Category

def create_category(name, limit):
    category = Category.create(
        id = uuid4(),
        name = name,
        limit = limit,
    )

    return category.id