
def checkio(opacity):
    age_counter = 0
    initial_opacity = 10000

    while True:
        if is_fib_numb(age_counter):
            initial_opacity -= age_counter
        else:
            initial_opacity += 1

        if initial_opacity == opacity:
            break
        age_counter += 1

    return age_counter

def fib(n):
    if n == 0 or n == 1: return n
    return fib(n - 1) + fib(n - 2)

def is_fib_numb(test_numb):
    fib_numb_counter = 0
    while True:
        fib_numb = fib(fib_numb_counter)
        if fib_numb > test_numb:
            return False
        elif fib_numb == test_numb:
            return True
        fib_numb_counter += 1


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"