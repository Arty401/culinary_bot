import itertools
import sqlite3
from typing import Iterable, Any


class Database:
    def __init__(self, path_to_db='db.data'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: Iterable[Any] = None, fetch_one: bool = None, fetch_all: bool = None,
                commit: bool = None):

        if not parameters:
            parameters = tuple()

        connect = self.connection
        cursor = connect.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connect.commit()

        if fetch_one:
            data = cursor.fetchone()

        if fetch_all:
            data = cursor.fetchall()

        return data

    def create_table_recipe(self):
        sql = '''
        CREATE TABLE Recipes (
        id integer primary key autoincrement not null,
        title varchar(255) NOT NULL,
        recipe text,
        ingredients text
        );
        '''

        self.execute(sql, commit=True)

    def add_recipe(self, title: str, recipe: str, ingredients: str):
        sql = '''
        INSERT INTO Recipes values (?, ?, ?, ?);
        '''

        index = self.count_recipes() + 1
        parameters = (index, title, recipe, ingredients)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_recipes(self):
        sql = '''
        SELECT * FROM Recipes;
        '''
        return self.execute(sql, fetch_all=True)

    @staticmethod
    def format_args(sql: str, parameters: dict):
        sql += ' AND '.join([
            f'{item} = ?' for item in parameters
        ])

        return sql, tuple(parameters.values())

    def select_recipe(self, **kwargs):
        sql = "SELECT * FROM Recipes WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters, fetch_one=True)

    def select_recipe_by_title(self, title: str):
        sql = f"SELECT title, recipe, ingredients " \
              f"FROM Recipes " \
              f"WHERE title LIKE ? OR  title LIKE ? OR title LIKE ?"
        parameters = (f'%{title}%', f'%{title.lower()}%', f'%{title.title()}%')
        return self.execute(sql, parameters, fetch_all=True)

    def select_recipes_by_ingredients(self, ingredients: str):
        sql = f"select title, recipe, ingredients from Recipes WHERE "
        ingredients = tuple(ingredients.split(', '))
        ingredients = itertools.permutations(iterable=ingredients)
        parameters = [', '.join(item) for item in itertools.chain(ingredients)]
        sql += " OR ".join([f'ingredients LIKE ?' for item in parameters])
        return self.execute(sql, parameters, fetch_all=True)

    def count_recipes(self):
        return self.execute("SELECT COUNT(*) FROM Recipes;", fetch_one=True)[0]

    def delete_recipe(self, title: str):
        sql = "DELETE FROM Recipes WHERE title = ?"

        return self.execute(sql, (title,), commit=True)
