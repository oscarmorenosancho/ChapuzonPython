# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 15:54:34 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/13 16:56:32 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (2019, 9, 25, 3, 30)

print("{1:0>2}/{2:0>2}/{0:0>4} {3:0>2}:{4:0>2}".format(*kata))