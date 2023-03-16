# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 13:25:09 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/16 15:46:27 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import random

def random_in_size(size: int) -> int:
    return int(random() * size)

def generator(text, sep=" ", option=None) -> list:
    '''Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
    option especifica si una acción se realizará sobre las sub-strings antes de 
    ser producidas. '''
    options = [None, "shuffle", "unique", "ordered"]
    if not isinstance(text, str):
        print ("ERROR")
        return None
    elif sep == None or sep == '':
        print ("ERROR")
        return None
    elif not option in options:
        print ("ERROR")
        return None
    else:
        lst = text.split(sep)
        ret_lst = []
        if option == "shuffle":
            while lst:
                inx = random_in_size(len(lst))
                it = lst.pop(inx)
                ret_lst.append(it)
        elif option == "unique":
            while lst:
                it = lst.pop(0)
                if not it in ret_lst:
                    ret_lst.append(it)
        elif option == "ordered":
            ret_lst = [*lst]
            ret_lst.sort()
        else:
            ret_lst = lst
        return ret_lst