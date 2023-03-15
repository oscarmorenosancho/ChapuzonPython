# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:26:27 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/15 12:38:42 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    values: list
    shape: tuple

    def __init__(self, values: list):
        if isinstance(values[0], list):
            self.values = values
            self.shape = (len(values), len(values[0]))
        else:
            self.values = [ values ]
            self.shape = (1, len(values))

    def __init__(self, size: int):
        self.values = []
        if size > 0:
            self.shape = (size, 1)
            for i in range(size):
                self.values.append([ float(i) ])
        else:
            self.shape = (1, 1)
            self.values = [ [ float (size) ] ]

    def __init__(self, interv: tuple):
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
