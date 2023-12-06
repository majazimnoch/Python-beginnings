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

# 2
# for i in range (10, -1, -1):
#     print(i, end=" ")
# print("GO!")

# 3a

# for i in range (1, 11, 1):
#     print(i, end=" ")

# # for i in range (10):
# #     print(i+1, end=" ")

# 3b

# number = int(input("How many numbers do you want to see: "))

# for i in range (1, number+1, 1):
#     print(i, end=" ")

# 3c

# start = int(input("choose the smallest number "))
# stop = int(input("choose the biggest number: "))

# for i in range (start, stop+1, 1):
#     print(i, end=" ")

# 3d

# start = int(input("choose the smallest number "))
# stop = int(input("choose the biggest number: "))
# intervallen = int(input("Choose an inetrval: "))

# for i in range(start, stop+1, intervallen):
#     print(i, end=" ")

# 4a

# summa = 0
# for i in range (1, 11, 1):
#    summa += i
# print(f'Summan is {summa}')

# # 4b

# number = int(input("Write how many numbers do you want to have: "))
# summa = 0
# for i in range (1, number+1, 1):
#    summa += i
#    print(i, end=" ")
# print(f'Summan is {summa}')

# 4c

# start = int(input("Write the smallest number: "))
# stop = int(input("Write the biggest number: "))

# number = int(input("Write how many numbers do you want to have: "))
# summa = 0
# for i in range (1, number+1, 1):
#    summa += i
#    print(i, end=" ")
# print(f'Summan is {summa}')

# # 4d
# summa = 0

# start = int(input("Write the smallest number: "))
# stop = int(input("Write the buggest number: "))
# intervallen = int(input("Choose the interval: "))

# for i in range(start,stop +1, intervallen):
#     summa += i
#     print(i, end=" ")
# print(f'Summan ar {summa}')

# # 5

# number = int(input("Write a number you want to multiply"))
# i = 1
# for i in range(1, 11, 1):
#     print(f'{i} x {number} = {i * number}')
#     i += 1

# # # # Tasks exercises med Blandade # # # #

print("kursutvärdering")
while True:
     svar = int(input("Betygsätt denna kurs med en siffra mellan 1-5: "))
     if svar == 5:
         break
     else:
         print("Du måste tryck fel, försök igen")

print("Tack, ditt omdöme om denna kurs har registrerats")

