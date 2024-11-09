from data.categories import Category

def update_category(id, name, limit):
    category = Category.get_by_id(id)
    
    category.name = name
    category.limit = limit

    category.save()