# x = 0
# while x < 10:
#     print(x)
#     x += 1

# y = 5
# while y != 0:
#     print(y)
#     y -= 1


# z = 10
# while z != 0:
#     print(z)

# color = input('Gissa vilken farg jag tanker pa: ')

# while color != 'gul':
#     color = input('fel, gissa igen: ')
# print('du gissade ratt')

# summa = 0
# k = 1

# while k <= 5:
#     summa += k
#     k += 1

# print('Resultat: ', summa)

# print(' ::: BILRESAN ::: ')
# while True:
#     print('My fragar: Ar vi framme snart?')
#     svar = input('Du: ')
#     if svar == 'ja':
#         break
#     elif svar == 'nej':
#         continue
#     elif 'glass' in svar:
#         print('my: Horde jag glass?')
#         svar = input('du: ')
#         if svar == 'ja':
#             print('My: jag vill ha glass genast')
#             continue
#     print('jag ar kissnodig!')
# print('My: Vilken tur')

# for i in range(10):
#     print(i)

# for hej in range(10):
#     print(hej)

# i = 5
# while i < 15:
#     print(i)
#     i += 2
# for i in range (5,10):
#      print(i)


# for i in range (25, 20, -2):
#     print(i)

# for x in range(5):
#     print('#', end = '')

# # # # Tasks exercises med WHILE # # # #

# TASK 0

# tal = int(input("Type a number: "))
# while tal < 100:
#     print(tal)
#     tal *= 1.5

# TASK 1 a

# i = 0
# while i <= 20:
#     print(i, end=" ")
#     i += 2
# print()

# TASK 1 b

# i = 20
# while i >= 0:
#     print(i, end=" ")
#     i -= 2
# print()

# # TASK 2

# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1
# print('GO!')

# # TASK 3 a

# i = 1
# while i < 10:
#     print(i, end=" ")
#     i += 1
# print()

# # TASK 3 b

# i = 1
# n = int(input("Write a number: "))
# while i <= n:
#     print(i, end= " ")
#     i += 1
# print()

# # TASK 3 c

# start = int(input("write min number: "))
# slut = int(input("write max number: "))

# while start <= slut:
#     print(start, end=" ")
#     start += 1
# print()

# # TASK 3 d 

# start = int(input("write min number: "))
# slut = int(input("write max number: "))
# intervalen = int(input("write how much you want to increase the number: "))

# while start <= slut:
#     print(start, end=" ")
#     start += intervalen
# print()

# # TASK 4 a

# i = 1
# summa = 0
# while i <= 10:
#     print(i, end=" ")
#     summa += i
#     i += 1
# print(f'Summan is {summa}')

# # TASK 4 b

# i = 1
# summa = 0
# n = int(input("Write a number: "))

# while i <= n:
#     print(i, end=" ")
#     summa += i
#     i += 1

# print(f'Summan is {summa}')

# # TASK 4 c

# start = int(input("Write the lowest number"))
# stop = int(input("Write the highest number"))
# summa = 0

# while start <= stop:
#     print(start, end=" ")
#     summa += stop
#     start += 1
# print(f'Summan is {summa}')

# # # TASK 4 d

# start = int(input("Write the lowest number: "))
# stop = int(input("Write the highest number: "))
# intervall = int(input("Which intervall do you want to have?: "))
# summa = 0

# while start <= stop:
#     print(start, end=" ")
#     summa += start
#     start += intervall
# print(f'Summan is {summa}')

# # # TASK 5

# number = int(input("write a number which you want to multiply: "))
# i = 1
# while i <= 10:
#     print(f'{i} x {number} = {i*number}')
#     i += 1


# # # # Tasks exercises med FOR # # # #

# for i in range(10):
#   print(i)

# 1a
# for i in range (0, 21, 2):
#     print(i, end=" ")

# 1b

# for i in range (21, -1, -2):
#     print(i, end=" ")