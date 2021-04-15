"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

print("Enter 'exit' for exit.")


def average_func():
    a = input("First - ")
    if a == "exit":
        return print("Good bye!")
    b = int(input("Second - "))
    c = int(input("Third - "))
    a = int(a)

    z = []
    z.append(a)
    z.append(b)
    z.append(c)
    if a == b or a == c:
        print(f"Average number -  {a}")
        print("+" * 100)
        return average_func()
    if c == b or c == a:
        print(f"Average number -  {c}")
        print("+" * 100)
        return average_func()
    if b == a or b == c:
        print(f"Average number -  {b}")
        print("+" * 100)
        return average_func()
    print("+" * 100)
    print(f'List -  {z}')
    k = max(z)
    l = min(z)
    print(f'Max & min - {k} & {l}')
    i = 0
    while i <= len(z):
        if z[i] != k:
            if z[i] != l:

                print(f"Average number -  {z[i]}")
                print("+" * 100)
                return average_func()
            else:
                i = i+1
        else:
            i = i+1


average_func()
