from data.categories import Category

def delete_category(id):
    category = Category.get_by_id(id)
    
    category.delete_instance()