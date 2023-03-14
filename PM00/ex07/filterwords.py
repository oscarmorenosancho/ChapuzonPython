# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 10:05:15 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/14 14:31:57 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string 

params = sys.argv[1:]
if (len(params) != 2):
	print('ERROR')
	exit(0)
if (not params[1].isnumeric()):
	print('ERROR')
	exit(0)

max_len = int(params[1])
words = params[0].translate(str.maketrans('', '', string.punctuation)).split()
filt_words = [w for w in words if len(w) > max_len]
print (filt_words)