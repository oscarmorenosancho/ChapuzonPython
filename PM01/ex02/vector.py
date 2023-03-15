# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:26:27 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/15 18:54:49 by omoreno-         ###   ########.fr        #
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
        elif isinstance(arg, float):
            self.initVector_float(int(arg))
        elif isinstance(arg, Vector):
            new_i = arg.copy()
            self.initVector_list(new_i.values)
        else:
            print ("Assertion error: argument is not a valid type")
            self.values = [[]]
            self.shape = (0, 0)

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

    def initVector_float(self, size: float):
        print("asd")
        int_size = int(size)
        nv = Vector(int_size)
        nv.add_float(100.0)
        self.values = nv.values
        self.shape = nv.shape

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
            return self

    def __copy__(self):
        values_list = []
        for i in range(self.shape[0]):
            col_list = []
            for j in range(self.shape[1]):
                col_list.append(self.values[i][j])
            values_list.append(col_list)
        return Vector(list(values_list))

    def copy(self):
        return self.__copy__()

    def __str__(self) -> str:
        return str(self.values)
    
    def __repr__(self)-> str:
        txt = "<Vector> class with shape: {0} and values: {1}"
        return (txt.format(self.shape, self.values))

    def dot(self, other) -> float:
        res = 0.0
        if not isinstance(other, Vector):
            print("Assertion Error: another Vector must be provided")
            return None
        elif self.shape != other.shape:
            print("Assertion Error: shape must be the same")
            return None
        else:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    res += float(self.values[i][j] * other.values[i][j])
            return res

    def T(self):
        values_list = []
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                values_list.append(self.values[i][j])
        nshape = (self.shape[1], self.shape[0])
        values_list2 = []
        k = 0
        for i in range(nshape[0]):
            col_list = []
            for j in range(nshape[1]):
                col_list.append(values_list[k])
                k += 1
            values_list2.append(col_list)
        return Vector(list(values_list2))

    def add_float(self, other: float):
        values_list = []
        for i in range(self.shape[0]):
            col_list = []
            for j in range(self.shape[1]):
                col_list.append(self.values[i][j] + other)
            values_list.append(col_list)
        return Vector(list(values_list))

    def add_int(self, other: int):
        return self.add_float(float(other))

    def add_Vector(self, other):
        if not isinstance(other, Vector):
            print("Assertion Error: another Vector must be provided")
            return None
        elif self.shape != other.shape:
            print("Assertion Error: Vector dimensions must match")
            return None
        else:
            values_list = []
            for i in range(self.shape[0]):
                col_list = []
                for j in range(self.shape[1]):
                    col_list.append(self.values[i][j] + other.values[i][j])
                values_list.append(col_list)
            return Vector(list(values_list))

    def mul_float(self, other: float):
        values_list = []
        for i in range(self.shape[0]):
            col_list = []
            for j in range(self.shape[1]):
                col_list.append(self.values[i][j] * other)
            values_list.append(col_list)
        return Vector(list(values_list))

    def mul_int(self, other: int):
        return self.mul_float(float(other))

    def mul_Vector(self, other):
        if not isinstance(other, Vector):
            print("Assertion Error: another Vector must be provided")
            return None
        elif self.shape != other.shape:
            print("Assertion Error: Vector dimensions must match")
            return None
        else:
            return self.dot(other)

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.add_Vector(other)
        elif isinstance(other, float):
            return self.add_float(other)
        elif isinstance(other, int):
            return self.add_float(float(other))
        else:
            print("Assertion error: other operand must be escalar or Vector")
            return None
    
    def __radd__(self, other):
        return self.__add__(self, other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.mul_Vector(other)
        elif isinstance(other, float):
            return self.mul_float(other)
        elif isinstance(other, int):
            return self.mul_float(float(other))
        else:
            print("Assertion error: other operand must be escalar or Vector")
            return None
    
    def __rmul__(self, other):
        return self.__mul__(self, other)
