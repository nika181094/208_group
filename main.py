# Задание 1
# a = int(input('Введите год: '))
# if a % 400 == 0:
#     print("%d високосный" %a)
# elif a % 100 == 0:
#     print("%d не високосный" %a)
# elif a % 4 == 0:
#     print("%d високосный" %a)
# else:
#     print("%d не високосный" %a)

#  Задание 2
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a + b > c and a + c > b and b + c > a:
#     print("Треугольник существует")
# else:
#     print("Треугольник не существует")

#  Задание 3
# import math
# print("Введите координаты точки и радиус круга")
# x = float(input("x = "))
# y = float(input("y = "))
# r = float(input("R = "))
# hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)
# if hypotenuse <= r_circle:
#     print("Точка принадлежит кругу")
# else:
#     print("Точка НЕ принадлежит кругу")

#  Задание 4 проверить совпадает ли введенное число с заданным,если да - вывести на экран "you win!", в противном случае вывести "try again!"
a = int(input('Введите число: '))
if a==42:
    print('You win!')
else:
    print('Try again!')