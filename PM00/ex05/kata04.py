# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 15:54:34 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/13 17:06:04 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (0, 4, 132.42222, 10000, 12345.67)
print("module_{0:0>2}, ex_{1:0>2} : {2:.5f}, {3:.2e}, {4:.2e}".format(*kata))