from data.categories import Category

def get_category(id):
    return Category.get_by_id(id)