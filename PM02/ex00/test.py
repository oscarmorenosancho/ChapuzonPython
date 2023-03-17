# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 11:36:29 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/17 15:43:52 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_reduce import *

lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# lst = []
concat = lambda u, v: u + v
res = ft_reduce(concat, lst, "(append here)->")
print (lst, " becomes ", res)

# from ft_map import *

# lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# res = ft_map(ord, lst)
# lres = list(res)
# print (lst, " becomes ", res, lres)

# from ft_filter import *

# lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# char_is_lower = lambda u: u.islower()
# res = ft_filter(char_is_lower, lst)
# lres = list(res)
# print (lst, " becomes ", res, lres)