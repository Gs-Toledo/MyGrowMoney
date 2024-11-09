from uuid import uuid4

from data.categories import Category

def create_category(name):
    category = Category.create(
        id = uuid4(),
        name = name
    )

    return category.id