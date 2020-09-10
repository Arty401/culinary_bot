from utils.db_api.sqlite import Database

db = Database()


def test():
    recipes = db.select_all_recipes()
    print(recipes)
    recipe1 = db.select_recipe_by_title("Test1")
    print(recipe1)
    recipe2 = db.select_recipe(title="Test2", recipe="test2")
    print(recipe2)


if __name__ == '__main__':
    test()
