#!/usr/bin/env python3

ROMAN_NUMS = (
    (1, "I"),
    (4, "IV"),
    (5, "V"),
    (9, "IX"),
    (10, "X"),
    (40, "XL"),
    (50, "L"),
    (90, "XC"),
    (100, "C"),
    (400, "CD"),
    (500, "D"),
    (900, "CM"),
    (1000, "M")
)

def checkio(input_number):
    """ solution """
    result_roman_numeral = ""

    for numb, roman_numb in reversed(ROMAN_NUMS):
        while input_number >= numb:
            input_number -= numb
            result_roman_numeral += roman_numb

    return result_roman_numeral

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
