# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 12:32:27 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/14 17:25:26 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

def count_set_instr(s :str, set :str) -> int:
    acum = 0
    for c in set:
        acum += s.count(c)
    return acum

def text_analyzer(s =None):
    """text_analyzer es una funcion que toma una string como parametro y 
    cuenta la cantidad de mayusculas, minusculas, signos de puntuacion y 
    espacios.
    Si el string proporcionado es None pide al usuario que introduzca
    un string
    """

    if s == None:
        s = input("The argument is invalid, Introduce a string >")
    if (not isinstance(s,str)):
        print ("AssertionError: argument is not a string")
    else:
        print ("The text contains {} character(s):"
            .format(len(s)))
        print ("- {} upper letter(s)"
            .format(count_set_instr(s, string.ascii_uppercase)))
        print ("- {} lower letter(s)"
            .format(count_set_instr(s, string.ascii_lowercase)))
        print ("- {} punctuation mark(s)"
            .format(count_set_instr(s, string.punctuation)))
        print ("- {} space(s)"
            .format(count_set_instr(s, string.whitespace)))

if __name__ == "__main__":
    params = sys.argv[1:]
    #if len(params) < 1:
    #    print("AssertionError: no argument is provided")
    if len(params) > 1:
        print("AssertionError: more than one argument are provided")
    elif len(params) < 1:
        text_analyzer()
    else:
        text_analyzer(params[0])