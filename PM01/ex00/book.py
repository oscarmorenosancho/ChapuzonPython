# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 09:17:15 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/15 10:52:04 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import *
from recipe import Recipe

class Book:
    name: str
    last_update: datetime
    creation_date: datetime
    recipes_list: dict

    def __init__(self,
                name: str,
                recipes_list: dict,
                creation_date: datetime =None):
        self.name = name
        self.recipes_list = recipes_list
        if not creation_date:
            self.creation_date = datetime.now()
        else:
            self.creation_date = creation_date
        self.last_update = self.creation_date

    def get_recipe_by_name(self, name):
        """Imprime la receta con el nombre \texttt{name}
        y devolver la instancia"""
        text = "\t {0}\n".format(self.name)
        print(text)
        return self

    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        else:
            print ("Assertion Error: you must provide an instance of Recipe")
            print ("this object: {}".format(recipe))
            print ("is not a Recipe")

    def __str__(self):
        """Return the string to print with the book info"""
        fmt = "Book\nname: {0}\ncreation date: {1}\nlast update: {2}\n"
        txt = fmt.format(self.name,
                        self.creation_date,
                        self.last_update)
        for rec_type in ['postre', 'comida','entrante']:
            txt += 'Recipes list of type {}:\n'.format(rec_type)
            for rec in self.get_recipes_by_types(rec_type):
                txt += str(rec)     
        return txt