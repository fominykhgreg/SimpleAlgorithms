"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
from timeit import timeit


def search_func(letter):
    if letter == 0:
        return print("Good bye.")
    if 26 < letter or letter < 1:
        print("Error number. Enter correct value.")
        return search_func(int(input("Enter letter number - ")))
    lst_alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    i = 0

    while lst_alfa[letter-1] != lst_alfa[i]:
        i = i+1
    else:
        print(f'Letter - "{lst_alfa[i]}". Press 0 for exit.')
        print("#" * 100)
        return search_func(int(input("Enter letter number - ")))


search_func(int(input("Enter letter number - ")))

# print(timeit('search_func(0)', globals = globals(), number = 10000))
