# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:26:27 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/15 13:45:34 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import overload

class Vector:
    values: list
    shape: tuple

    def __init__(self, arg):
        if isinstance(arg, list):
            self.initVector_list(arg)
        elif isinstance(arg, tuple):
            self.initVector_tuple(arg)
        elif isinstance(arg, int):
            self.initVector_int(arg)
        else:
            self.initVector_list(arg)
        
    def initVector_list(self, values: list):
        if isinstance(values[0], list):
            self.values = values
            self.shape = (len(values), len(values[0]))
        else:
            self.values = [ values ]
            self.shape = (1, len(values))

    def initVector_int(self, size: int):
        self.values = []
        if size > 0:
            self.shape = (size, 1)
            for i in range(size):
                self.values.append([ float(i) ])
        else:
            self.shape = (1, 1)
            self.values = [ [ float (size) ] ]

    def initVector_tuple(self, interv: tuple):
        self.values = []
        self.shape = (0, 0)
        if len(interv) != 2:
            print("Assertion error: the interval must contain 2 values")
            return None
        elif interv[0] >= interv[1]:
            print("Assertion error: the interval start must be smaller")
            return None
        else:
            size = int(interv[1] - interv[0])
            self.shape = (size, 1)
            for i in range(size):
                self.values.append([ float(i) + interv[0]])

    def __str__(self) -> str:
        return str(self.values)
    
    def __repr__(self)-> str:
        txt = "<Vector> class with shape: {0} and values: {1}"
        return (txt.format(self.shape, self.values))

    def __add__(self, other):
        if not isinstance(other, Vector):
            print("Assertion Error: another Vector must be provided")
            return None
        elif self.shape != other.shape:
            print("Assertion Error: Vector dimensins must match")
            return None
        else:
            values_list = []
            for i in range(self.shape[0]):
                col_list = []
                for j in range(self.shape[1]):
                    col_list.append(self.values[i][j] + other.values[i][j])
                values_list.append(col_list)
            nv = Vector(list(values_list))
            return nv
                    