#!/usr/bin/env python3

def recall_password(cipher_grille, ciphered_password):
    """ solution """
    unciphered_password = ""
    step = 4

    while step >= 1:
        unciphered_password += read_letters(cipher_grille, ciphered_password)
        cipher_grille = rotate_grille(cipher_grille)
        step -= 1
    return unciphered_password

def read_letters(cipher_grille, ciphered_password):
    letters = ""

    for row in range(len(cipher_grille)):
        for column in range(len(cipher_grille[row])):
            if cipher_grille[row][column] == 'X':
                letters += ciphered_password[row][column]

    return letters

def rotate_grille(cipher_grille):
    new_cipher_grille = []
    new_row = ""

    for row in range(len(cipher_grille)):
        for column in reversed(range(len(cipher_grille[row]))):
            new_row += cipher_grille[column][row]
        new_cipher_grille.append(new_row)
        new_row = ""

    return new_cipher_grille


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
