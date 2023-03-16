# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 09:03:30 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/16 11:56:39 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
    name: str
    cooking_lvl: int
    cooking_time: int
    ingredients: list
    description: str
    recipe_type: str

    def __init__(self, name: str, 
                 cooking_lvl: int, 
                 ingredients: list,
                 recipe_type: str,
                 description: str=None):
        """initializator / constructor of Recipe"""
        err_msg = "Assertion error: "
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.ingredients = ingredients
        allowed_types = ['postre', 'comida','entrante']
        self.recipe_type = recipe_type
        if not recipe_type in allowed_types:
            print (err_msg + f"recipe_type must be in: {allowed_types}")
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        fmt = "Recipe\nname: {0}\nlevel: {1}\ntype: {2}\n"
        txt = fmt.format(self.name,
                        self.cooking_lvl,
                        self.recipe_type)
        if self.description != None:
            txt += 'description: {}\n'.format(self.description)
        txt += 'ingredients:\n'
        for ing in self.ingredients:
            txt += '\t' + ing + '\n'    
        return txt
