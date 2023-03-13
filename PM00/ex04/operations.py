# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 15:27:28 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/13 15:52:13 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == "__main__":
    import sys
    params = sys.argv[1:]
    #if len(params) < 1:
    #    print("AssertionError: no argument is provided")
    if len(params) > 2:
        print("AssertionError: too many arguments")
    elif len(params) < 1:
        print("AssertionError: too few arguments")
    else:
        if not (params[0].isnumeric() and params[1].isnumeric):
            print("AssertionError: only integers")
        else:
            nbr1 = int(params[0])
            nbr2 = int(params[1])
            print("Sum:\t{}".format(nbr1 + nbr2))
            print("Difference:\t{}".format(nbr1 - nbr2))
            print("Product:\t{}".format(nbr1 * nbr2))
            if (nbr2 == 0):
                print("ERROR (division by zero)")
                print("ERROR (modulo by zero)")
            else:
                print("Quotient:\t{}".format(nbr1 / nbr2))
                print("Remainder:\t{}".format(nbr1 % nbr2))
