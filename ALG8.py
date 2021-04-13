"""
Определить, является ли год, который ввел пользователем, високосным или не високосным.
"""


def intercalary_year_chek_func():
    print("!" * 100)
    year = int(input("What's year you want? - "))
    if year == 0:
        return print(f"################################\nGood bye.\nExit.")
    if year % 400 == 0:
        print(f"Intercalary year. {year}")
        return intercalary_year_chek_func()
    if year % 100 == 0:
        print(f"Not intercalary year. {year}.")
        return intercalary_year_chek_func()
    if year % 4 == 0:
        print(f"Intercalary year. {year}")
        return intercalary_year_chek_func()
    else:
        print(f"Not intercalary year. {year}")
        return intercalary_year_chek_func()
    # print("Not intercalary year")


intercalary_year_chek_func()
