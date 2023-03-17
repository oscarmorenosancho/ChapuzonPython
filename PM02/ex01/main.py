# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 16:28:38 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/17 18:20:01 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
    
def what_are_the_vars(*argv, **kwargs): 
    """
    ...
    """
    if (argv and is_iterable(argv)) or kwargs:
        objC = ObjectC()
    else:
        objC = None
    if argv and is_iterable(argv):
        i = 0
        for arg in argv:
            setattr(objC, 'var_'+str(i), arg)
            i += 1
    if kwargs:
        for arg in kwargs:
            setattr(objC, arg, kwargs[arg])
    return objC 

class ObjectC(object):
    def __init__(self):
        return

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a= 10, var_2="world")
    doom_printer(obj)