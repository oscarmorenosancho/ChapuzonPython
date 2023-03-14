# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 16:18:20 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/14 16:47:02 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random as rd

greeting = """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game. 
Good luck!
"""
prompt = "What's your guess between 1 and 99?\n>> "
congrat = "Congratulations, you've got it!"
won_msg = "You won in {} attempts!"
too_high = "Too high!"
too_low = "Too low!"
nan_msg = "That's not a number."
goodbye = "Goodbye!"
iter = 1
target = rd.randint(1, 99)
print (greeting)
while True:
    guess = 0
    while guess == 0:
        guess_str = input(prompt)
        if guess_str == 'exit':
            print(goodbye)
            exit(0)
        if not guess_str.isnumeric():
            print(nan_msg)
        else:
            guess = int(guess_str)
    if guess == target:
        print(congrat)
        print(won_msg.format(iter))
        exit(0)
    elif guess > target:
        print(too_high)
    else:
        print(too_low)
    iter += 1