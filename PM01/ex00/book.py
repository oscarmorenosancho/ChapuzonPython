# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 09:17:15 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/16 11:51:19 by omoreno-         ###   ########.fr        #
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

    def get_recipe_by_name(self, name) -> Recipe:
        """Imprime la receta con el nombre \texttt{name}
        y devolver la instancia"""
        err_msg = "Assertion error: "
        allowed_types = ['postre', 'comida','entrante']
        rec = None
        i = 0
        allowed_types_len = len (allowed_types)
        while (rec == None and i < allowed_types_len):
            rec_arr = [r for r in self.recipes_list[allowed_types[i]] if r.name == name]
            if rec_arr:
                rec = rec_arr[0]
            i += 1
        if (rec):
            text = f"\t {rec}\n"
            print(text)
        else:
            err_msg + f"receipt named {name} not found"
        return rec

    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        err_msg = "Assertion error: "
        if not isinstance(recipe, Recipe):
            print (err_msg + "you must provide an instance of Recipe")
            print (f"this object: {recipe}")
            print ("is not a Recipe")
        elif not recipe.recipe_type in ['postre', 'comida','entrante']:
            print (err_msg + "the receipt is not a valid recipe type")
            print (f"this object {recipe.name} type: {recipe.recipe_type}")
            print ("is not a valid recipe type")
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()

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