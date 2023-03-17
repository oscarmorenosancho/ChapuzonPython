# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 11:18:51 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/17 15:11:03 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import functools

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
    
def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable. Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator). Return:
    An iterable.
    None if the iterable can not be used by the function. """
    if (is_iterable(iterable)):
        for it in iterable:
            if function_to_apply(it):
                yield it
    else:
        raise TypeError("the second argument must be iterable")
