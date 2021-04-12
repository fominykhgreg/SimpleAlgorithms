"""
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""


def triangle_chek():
    a = int(input("Enter first length: "))
    b = int(input("Enter second length: "))
    c = int(input("Enter third length: "))
    print("/" * 30)
    if a < b+c or b > a+c or c > a+b:
        print("This triangle available.")
    else:
        print("This triangle does not exist.")

    if a == b & a == c:
        print("Equilateral triangle.")
    elif a == b or a == c:
        print("Isosceles triangle.")


triangle_chek()
