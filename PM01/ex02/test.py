# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:26:22 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/16 13:19:51 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import *
import sys

try:
    v1 = Vector(5)
    v2 = Vector((5, 10))

    v3 = v2 * v1
    v4 = v1 / 10
    v5 = 100 - v1

    print (f"v1: {v1}")
    print (f"v2: {v2}")
    print (f"v3: {v3}")
    print (f"v4: {v4}")
    print (f"v5: {v5}")
    v6 = 1 / v1

except Exception as e:
    ex_type, ex_value, ex_traceback = sys.exc_info()
    print(f"{ex_type.__name__}: {ex_value}")