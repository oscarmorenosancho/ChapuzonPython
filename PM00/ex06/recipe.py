# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 17:14:55 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/14 12:37:52 by omoreno-         ###   ########.fr        #
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
    line = "Recipe for {}:".format(recipe_name)
    print (line)
    ingredients = recipe["ingredients"]
    meal = recipe["meal"]
    line = "Ingredients list: {} To be eaten for {}.".format(ingredients, meal)
    print (line)
    line = "Takes {} minutes of cooking.".format(recipe["prep_time"])
    print (line)

def delete_recipe(cb: dict, recipe_name: str):
	if recipe_name in cb:
		del cb[recipe_name]

def add_recipe(cb: dict, recipe_name: str, recipe_dict):
    cb.update({recipe_name: recipe_dict})

def input_recipe() -> dict:
    meal = input("Enter the meal>")
    prep_time = -1
    while prep_time < 0:
        prep_time_str = input("Enter the preparation time>")
        if prep_time_str.isnumeric():
            prep_time = int(prep_time_str)
        else:
             print("Assertion Error: value is not a number, try again")
    ingredients = []
    msg = "Enter an ingredient name to add it, empty to finish>"
    while True:
        ingredient = input(msg)
        if ingredient == '':
            break
        else:
             ingredients.append(ingredient)
    return ({'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time})

def input_command() -> str:
    prompt_msg = """Welcome to the Python Cookbook !
List of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit

Please select an option:
>> """
    return input(prompt_msg)

if __name__ == "__main__":
    cmd = 0
    recipe_name = ''
    while cmd != '5':
        cmd = input_command()
        print('')
        if cmd == '1':
            msg = "Please enter a recipe name to add it:\n>>"
            recipe_name = input(msg)
            print('')
            rec = input_recipe()
            print('')
            add_recipe(cookbook, recipe_name, rec)
        elif cmd == '2':
            msg = "Please enter a recipe name to delete it:\n>>"
            recipe_name = input(msg)
            print('')
            delete_recipe(cookbook, recipe_name)
        elif cmd == '3':
            msg = "Please enter a recipe name to get its details:\n>>"
            recipe_name = input(msg)
            print('')
            print_recipe_details(cookbook, recipe_name)
            print('')
        elif cmd == '4':
            print_recipe_names(cookbook)
            print('')
        elif cmd == '5':
            msg = "Cookbook closed. Goodbye !"
            print (msg)
