from data.categories import Category

def get_all_categories():
    return Category.select().execute()