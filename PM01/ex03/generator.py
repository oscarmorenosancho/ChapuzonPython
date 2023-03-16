# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 13:25:09 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/16 13:57:01 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import random

def random_in_size(size: int) -> int:
    return int(random() * size + 1)

def generator(text, sep=" ", option=None) -> list:
    '''Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
    option especifica si una acción se realizará sobre las sub-strings antes de 
    ser producidas. '''
    options = [None, "shuffle", "unique", "ordered"]
    if not isinstance(text, str):
        raise AssertionError("first argument must be a string")
    elif sep == None or sep == '':
        msg = f"separator can not be None or Empty"
        raise AssertionError(msg)
    elif not option in options:
        msg = f"option can only be in {options[1:]} or not specified"
        raise AssertionError(msg)
    else:
        lst = text.split(sep)
        print (random_in_size(len(lst)))
        return lst