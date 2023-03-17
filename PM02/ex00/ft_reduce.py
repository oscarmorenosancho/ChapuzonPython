# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 11:18:56 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/17 15:42:12 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import functools

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def ft_map_over(function_to_apply, iterable, initialize = None):
    if (is_iterable(iterable)):
        prev = initialize
        for it in iterable:
            prev = function_to_apply(prev, it)
            yield prev
    else:
        raise TypeError("the second argument must be iterable")

def ft_reduce(function_to_apply: callable, iterable, initializer = ''):
    """Apply function of two arguments cumulatively. Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator). Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function. """
    if (is_iterable(iterable)):
        #return functools.reduce(function_to_apply, iterable, initializer)
        lst = list(ft_map_over(function_to_apply, iterable, initializer))
        if (len(lst) > 0):
            return lst[-1]
        else:
            return initializer
    else:
        raise TypeError("the second argument must be iterable")
