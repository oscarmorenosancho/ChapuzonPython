# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 12:32:27 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/13 13:23:49 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def count_set_instr(s :str, set :str) -> int:
    acum = 0
    for c in set:
	    acum += s.count(c)
    return(acum)

def text_analyzer(s :str =None):
    """text_analyzer es una funcion que toma una string como parametro y 
    cuenta la cantidad de mayusculas, minusculas, signos de puntuacion y 
    espacios.
    Si el string proporcionado es None pide al usuario que introduzca
    un string
    """
    majus = "ABCDEFGHIJKLMNPQRSTUVWXYZ"
    minus = majus.swapcase()
    punt_mark = ",.;:?!"
    spaces = " "

    if s == None:
        print ("Input a string")
    else:
       print (count_set_instr(s, majus))
       print (count_set_instr(s, minus))
       print (count_set_instr(s, punt_mark))
       print (count_set_instr(s, spaces))
