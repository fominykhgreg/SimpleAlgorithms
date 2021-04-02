"""Написать программу, которая генерирует в указанных пользователем границах
случайное целое число,
случайное вещественное число,
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно. """


def diapazon(a, b):
    if a == b:
        return str(a)
    else:
        if a > b:
            return f'{str(a)}, {str(diapazon(a-1, b))}'
        else:
            return f'{str(a)}, {str(diapazon(a+1, b))}'


print(diapazon(43, 34))
