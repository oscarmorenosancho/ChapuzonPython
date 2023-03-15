# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 09:42:45 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/15 10:52:30 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from book import Book

tarta = Recipe("tarta", 3, ['harina', 'huevo', 'azúcar', 'levadura'], 'postre',
               'bizcocho')
to_print = str(tarta)
print("\nprint just tarta")
print(to_print)
recipe_list = {'postre': [tarta],'comida': [],'entrante': []}
book = Book('Caseras', recipe_list)
print("\nbefore updating")
print (book)
ensalada = Recipe("ensalada", 3, ['lechuga', 'aceite', 'vinagre', 'queso'], 'entrante')
book.add_recipe(ensalada)
cocido = Recipe("cocido", 3, ['lentejas', 'chorizo', 'cebolla'], 'comida')
book.add_recipe(cocido)
book.add_recipe(['sda', "asd"])
print("\nafter updating")
print (book)
