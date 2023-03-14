# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 12:06:38 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/14 17:29:03 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

params = sys.argv[1:]
if len(params) < 1:
    print("AssertionError: no argument is provided")
elif len(params) > 1:
    print("AssertionError: more than one argument are provided")
elif not params[0].isnumeric():
    print("AssertionError: argument is not an integer")
else:
    number = int(params[0])
    if number == 0:
        print("I'm Zero.")
    elif not number % 2:
        print("I'm Even.")
    else:
        print("I'm Odd.")
