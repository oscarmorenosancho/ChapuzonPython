# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 18:30:47 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/17 18:33:50 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from csvreader import CsvReader
if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        if file == None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()

    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
