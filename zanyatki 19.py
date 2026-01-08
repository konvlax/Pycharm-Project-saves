# import random
# a = random.randint(1, 10000)
# print(a)
# def draw_box(height, width):
#     for i in range(height):
#         print('*' * width)
#     print()
#
#
# draw_box(5, 7)
# draw_box(4, 4)
# draw_box(3, 9)
# birds = 5000
#
#
# def print_texas():
#     print('В Техасе обитает', birds, 'птиц')
#
#
# def print_california():
#     print('в калифорнии обитает', birds, 'птиц')
#
#
# print_texas()
# print_california()
# def convert_to_celsius(temp):
#     result = (5/9) * (temp - 32)
#     return result
#
#
# temp = float(input('введите колво градусов по Фарингейту:'))
# celsius = convert_to_celsius(temp)
# print(celsius)
# def compute_hypotenuse(a, b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return c
#

# print(compute_hypotenuse(3, 4))
# print(compute_hypotenuse(5, 12))
# print(compute_hypotenuse(1, 1))
# x = int(input())
# y = int(input())
#
# hypotenuse = compute_hypotenuse(x, y)
# print(hypotenuse)
# x1 = float(input())
# x2 = float(input())
# y1 = float(input())
# y2 = float(input())
#
#
# def get_distance(x1, y1, x2, y2):
#     return compute_hypotenuse(x1 - x2, y1 - y2)
#
#
# print(get_distance(x1, y1, x2, y2))
# n = int(input())
#
#
# def sum_digit(n):
#     result = 0
#     while n > 0:
#         result += n % 10
#         n //= 10
#     return result
#
#
# print(sum_digit(n))
# numbers = [1, 3, 5, 1, 6, 8, 10, 2]
#
#
# def solve_average(numbers):
#     return sum(numbers) / len(numbers)
#
#
# print(solve_average(numbers))
# def triple(num):
#     num = num * 3
#     return num
#
#
# print(triple(4))
# def triple(num):
#     print(num * 3)
#     return num * 3
#
#
# print(triple(4))
# def do_smth(numbers):
#     result = 1
#     for i in numbers:
#         result *= i
#
#     return result
#
#
# print(do_smth([2, 2, 2, 2]))
# def date_format(day, month, year):
#     return f'{year}-{month}-{day}'
#
#
# print(date_format(31, 10, 2025))
# def get_highest(names, heights):
#     max_height = max(heights)
#     index_max_height = heights.index(max_height)
#     return names[index_max_height]
#
#
# print(get_highest(['Андрей', 'валерия', 'Елена', 'Николай', 'Жанна'],
#                   [1.75, 1.61, 1.65, 1.83, 1.64]))
# def draw_box():
#     print('*' * 10)
#     for i in range(14):
#         print('*        *')
#     print('*' * 10)
#
#
# draw_box()
# def draw_triangle():
#     for i in range(10):
#         print('*' * i)
#
#
# draw_triangle()
# def con_to_mile(km):
#     mile = km * 0.6214
#     return mile
#
#
# print(con_to_mile(1))
def math_round(num):
    num1 = num - num // 1
    if num1 >= 0.50:
        num2 = num // 1 + 1
    else:
        return


print(math_round(1.52))
