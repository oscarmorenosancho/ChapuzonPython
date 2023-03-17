# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 18:24:54 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/17 18:59:29 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
    # ... Your code here ...
        print('init method called')
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        return

    def __enter__(self):
    # ... Your code here ...
        print('enter method called')
        #open file
        if self.filename:
            try:
                self.fhand = open(self.filename)
                #add a second argument to open in write mode
                # with 'w' to discard content n write
                # with 'a' to append content
                # with 'x' to create the file
            except:
                print('File nout found and can not be opened:', self.filename)
                exit()
        else:
            print("File open error: you must provide a filename")
        return
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
    # ... Your code here ...
        print('exit method called')
        #close file
        if (self.fhand):
            self.fhand.close()
        return
    
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
            Return:
                nested list (list(list, list, ...)) representing the data.
        """
        # ... Your code here ...
        for line in self.fhand:
            print(repr(line)) 
    
    def getheader(self):
        """ Retrieves the header from csv file.
            Returns:
                list: representing the data (when self.header is True). 
                None: (when self.header is False).
        """
