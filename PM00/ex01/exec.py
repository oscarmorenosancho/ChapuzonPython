# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcel>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 12:06:04 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/13 12:06:20 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

params = sys.argv[1:]
line = ""
if len(params) < 1:
    print("No argument was given\n")
else:
    rev_params = params[::-1]
    for x in rev_params:
        line += x[::-1].swapcase() + " "
    print(line.strip())
