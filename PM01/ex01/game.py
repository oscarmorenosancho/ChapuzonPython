# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 10:55:29 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/15 11:17:11 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    first_name: str
    is_alive: bool =True
    def __init__(self, first_name: str, is_alive: bool =True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

class Lannister(GotCharacter):
    def __init__(self, first_name=None):
        super().__init__(first_name=first_name)
        self.family_name = "Lannister"
        self.house_words = "Winter is never Going"
        self.weapons = ['sword', 'shield']
    
    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False