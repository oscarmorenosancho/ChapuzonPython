# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 16:48:22 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/14 18:23:25 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import sys

def ft_progress(lst: list) -> int:
    it = 0
    lim = len(lst)
    start_time = time.time()
    percent_prog = 0
    estimated_time = 0
    ind_prog = 0
    while it < lim:
        #"ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s"
        fmt = "ETA: {0:.2f}s [{1:0>3}%][{5:=>7}] {2}/{3} | elapsed time {4:.2f}s"
        str_prog = '>'
        if lim != 0:
            percent_prog = int(float(it + 1) / float(lim) * 100)
            ind_prog = 7 - int(percent_prog / (100.0 / 7.0))
            for rep in range(ind_prog):
                str_prog += ' '
        elapsed_time = time.time() - start_time
        if percent_prog != 0:
            estimated_time = elapsed_time * 100 / percent_prog
        line = fmt.format(estimated_time, percent_prog, it + 1, lim, elapsed_time, str_prog)
        print (line, sep='', end='\r', file=sys.stdout, flush=True)
        yield lst[it]
        it += 1

if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret+=(elem+3) %5
        time.sleep(0.01)
    print()
    print(ret)
