from data.categories import Category

def delete_category(id):
    category = Category.get_by_id(id)
    
    if category is not None:
        category.delete_instance()