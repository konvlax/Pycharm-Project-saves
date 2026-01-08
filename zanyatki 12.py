# import random
# a = random.randint(1, 10000)
# print(a)
# c = False
# while a != 0:
#     b = a % 10
#     if b == 7:
#         c = True
#     a = a // 10
# if c == True:
#     print('7')
# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)
# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#         break
# if flag is True:
#     print('число простое')
# else:
#     print('число составное')
# n = int(input())
# flag = False
# while n != 0:
#     last_digit = n % 10
#     if last_digit == 7:
#         flag = True
#         break
#     n //= 10
# if flag is True:
#     print('число содержит цифру 7')
# else:
#     print('число не содержит цифру 7')
# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue
#     print(i)
# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break
# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)
# mult = 1
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     if i % 9 == 0:
#         break
#     mult *= i
#     print(i)
# print(mult)
# n = int(input())
# i = 1
# for i in range(1, 100000):
#     if n % i == 0 and i != 1:
#         break
# print(i)
# n = int(input())
# t = False
# while n != 0:
#     ld = n % 10
#     if ld == 1:
#         t = True
#         break
#     n //= 10
# if t is True:
#     print("есть единица")
# else:
#     print("нет")
# a = int(input())
# for i in range(1, a + 1):
#     if 5 <= i <= 9:
#         continue
#     elif 17 <= i <= 37:
#         continue
#     elif 78 <= i <= 87:
#         continue
#     print(i)
# n = int(input())
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)
# a = int(input())
# b = 0
# c = 0
# while a != -1:
#     if a > 7:
#         b = b + a
#         c = c + 1
#     a = int(input())
# print(b /c)aadadada