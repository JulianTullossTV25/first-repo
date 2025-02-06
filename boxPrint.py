import pygame

def boxPrint():
    string = input('Give statement: ')
    words = string.split()
    longestWord = ""
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word
    print('*' * (len(longestWord) + 4))
    for word in words:
        print('* ' + word + ' '*(len(longestWord) - len(word)) + ' *')
    print('*' * (len(longestWord) + 4))

boxPrint()