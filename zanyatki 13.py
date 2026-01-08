# import random
# b = False
# a = random.randint(1, 1000)
# print(a)
# while a != 0:
#     ld = a % 10
#     if ld == 7:
#         b = True
#         break
#     a //= 10
# if b is True:
#     print('в числе есть 7')
# else:
#     print('нет 7')
# for hours in range(24):
#     for mins in range(60):
#         for sec in range(60):
#             print(hours, ':', mins, ':', sec)
# for i in range(3):
#     for j in range(3):
#         print(i, j)
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             break
#         print(i, j)
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         print(i, j)
# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)
# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end=' ')
# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)
# n = int(input())
# if n <= 0:
#     print('N должно быть больше 0')
# for i in range(n):
#     if n >= 10:
#         print('N должно быть меньше 10')
#         break
#     for b in range(3):
#         print(n, end=" ")
#     print(sep=" ")
# n = int(input())
#
# if n <= 0:
#     print('N должно быть больше 0')
# for i in range(n):
#     i += 1
#     if n >= 10:
#         print('N должно быть меньше 10')
#         break
#
#     for b in range(5):
#         print(n, end=' ')
#
#     print(sep=" ")
# a = int(input())
# j = 3
# for i in range(1, a + 1):
#     for i in range(1, 10):
#         c = i + j
#         print(j, "+", i, '=', c)