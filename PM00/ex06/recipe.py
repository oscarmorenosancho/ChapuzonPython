# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 17:14:55 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/13 18:15:33 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
    "bocadillo": 
    {
    	"ingredients": ["jamón", "pan", "queso", "tomate"],
        "meal": "almuerzo",
        "prep_time": 10
    },
    "tarta":
    {
    	"ingredients": ["harina", "azúcar", "huevos"],
        "meal": "postre",
        "prep_time": 60
    },
    "ensalada":
    {
    	"ingredients": ["aguacate", "rúcula", "tomates", "espinacas"],
        "meal": "almuerzo",
        "prep_time": 15
    }  
}

def print_recipe_names(cb: dict):
    for recipe in cb:
        print(recipe)

def print_recipe_details(cb: dict, recipe_name: str):
    recipe = cb[recipe_name]
    print("Ingredients")
    for ing in recipe["ingredients"]:
        print ("\t{}".format(ing))
    print("Meal")
    print("\t{}".format(recipe["meal"]))
    print("Preparation time")
    print("\t{}".format(recipe["prep_time"]))

def delete_recipe(cb: dict, recipe_name: str):
	if recipe_name in cb:
		del cb[recipe_name]
