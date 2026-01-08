# import random
# n = int(input())
# while n != 0:
#     last_digit = n % 10
#     n = n // 10
#     print(n)
# num = random.randint(1, 100)
# print(num)
# has_seven = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
# if has_seven == True:
#     print('YES🤑🤑🤑😇😇😇😎😎😎😼😼😼')
# else:
#     print('NO🤬🤬🤬😡😡😡👹👹👹👺👺👺')\

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)
# num = 123456789
# total = 0
# while num != 0:
#
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
#
# print(total)
# a = int(input())
# while a != 0:
#     n = a % 10
#     print(n)
#     a = a // 10
# a = int(input())
# t = 0
# m = 1
# y = 0
# c = 0
# j = 0
# l = 0
# v = a % 10
# p = 0
# while a != 0:
#     b = a % 10
#
#     t = t + b
#     m = m * b
#     y += 1
#     a = a // 10
#     j = t / y
#     if a == 0:
#         l = b
#     p = l + v
# print('произведение чисел:', m)
# print('колво чисел:', y)
# print('арифметическое чисел:', j)
# print('первая цифра:', l)
# print('сумма первой и последней цифры:', p)
# a = int(input())
# b = 0
# h = False
# while a != 0:
#     b = a % 10
#     a = a // 10
#     v = a % 10
#
#     if b == v:
#         h = True
#     if b != v:
#         h = False
#
# if h == True:
#     print('равны')
# if h == False:
#     print('нет')
