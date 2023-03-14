# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 14:44:27 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/14 16:11:38 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse_trans = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..', 
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'}

def translate_char_to_morse(c: chr) -> str:
    return (morse_trans[c])

def translate_word_to_morse(word: str) -> str :
    morse_word = list(map(translate_char_to_morse, word))
    return ' '.join(morse_word)

def translate_words_to_morse(words: str) -> str:
    morse_words = list(map(translate_word_to_morse, words))
    return ' / '.join(morse_words)

params = sys.argv[1:]
if len(params) < 1:
    exit(0)
text = ' '.join(params)
text = text.upper()
words = text.split()
all_alpha = 1
for word in words:
    all_alpha &= word.isalnum()
if not all_alpha:
    print("ERROR")
    exit(0)
print(translate_words_to_morse(words))