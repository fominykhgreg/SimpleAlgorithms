"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""


def letter_func(x, y):
    lst_alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    print("*" * 100)
    #print(len(lst_alfa))
    i = 0
    while x != lst_alfa[i]:
        i = i+1
    else:
        print(f'Буква "{x}" является {i+1}-ой в алфавитном порядке.')


    j = 0
    while y != lst_alfa[j]:
        j = j+1
    else:
        print(f'Буква "{y}" является {j+1}-ой в алфавитном порядке.')

    # num=abs(j-i)
    # print(i)
    # print(j)
    print("*"*100)
    num = abs((j-i)-1)
    print(f'Length through : {num}')

enter_letter1 = input("First letter: ").lower()
enter_letter2 = input("Second letter: ").lower()
# print(enter_letter1)
letter_func(enter_letter1, enter_letter2)
