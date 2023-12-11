# print('1\tJeh')
# print('1hej\rJeh')

# a = "Hello world"
# i = a.startswith('Hello')

# print(i)


# a = "Hello world"
# i = a.islower()

# print(i)

# a = "Hello world"
# i = a.strip()

# print(i)

# a = "Hello world"
# i = a.replace("Hello", "Good day")

# print(i)

# a = "Hello world"
# i = a.center(20)

# print(i)
# print(30 * '-')

# a = "Hello world"
# t = "z"
# i = a.find(t)

# print(i)

# len('en strang')

# while True:
#     name = input('write your name: ')
#     print('Your name has', len(name), 'characters.')

# chars = 'abcdef'

# print(chars[2])

# 25

# chars = 'ABCDEF'

# a = chars[-5]

# print(a)

# a = 'good day everyone'

# b = a[-3:]

# print(b)

# chars = 'ABCDEF'

# i = 0
# while i < len(chars):
#     print(i)
#     i += 1


# chars = 'ABCDEF'

# i = 0
# while i < len(chars):
#     print(chars[i])
#     i += 1


# chars = 'ABCDEF'

# for i in range(len(chars)):
#     print(chars[i])

# chars = 'ABCDEF'

# for char in chars:
#     print(char)


# name = "Anna"
# age = 50
# # description = name + ' ar ' + str(age) + ' ar gammal.'


# description = f'{name} is {age} ar gammal'
# print(description)

# rensa terminalfonster 
# import os
# os.system('clear')

# users = [
#     'Vlad',
#     'DanielB',
#     'DanielU',
#     'Jonathan',
#     'Martin'
# ]

# print(users)

# users[1] = 'Ida'

# users[3] = 'Martin'

# print(users)


# users = [
#      'Vlad',
#      'DanielB',
#      'DanielU',
#      'Jonathan',
#      'Martin'
#  ]


# users.append('Ida')

# del users[0]
# removed_user = users.pop(1)

# print(users) 
# # adds Ida
# print(removed_user)

# numbers = [6, 3, 1, 5]

# # print(numbers)

# # numbers.sort()

# # print(numbers)

# # numbers.remove(5)
# # print(numbers)

# numbers.clear()
# print()

# # users = ['Maria', 'Anna', 'Eva', 'Erik', 'Lars', 'Karl']

# s = users[:2]

# print(s)

# users = ['lina', 'gunilla', 'erik']

# i = 0
# while i < len(users):
#     print(users[i])
#     i += 1
 
# users = ['Maria', 'Anna', 'Eva', 'Erik', 'Lars', 'Karl']

# for user in users:
#     print('-', user)

# call_queue = []

# while True:
#     print('\n', call_queue, '\n')
#     operation = input('Operation: ')
#     if operation == 'in':
#         number = input('Lagg in > ')
#         call_queue.append(number)
#     elif operation == 'ut':
#         print('Tog ut >', call_queue[0])
#         del call_queue[0]


#         call_queue.pop()

 # LISTOR OCH REFERENSER 


# a = [1, 3, 7]
# b = a.copy( )
# b[1] = 5
# print(a)
# print(b)

# board = [
#     ['x', '', '0'],
#     ['0', 'x', ''],
#     ['', '', 'x'],
# ]

# for row in board:
#     for column in row:
#         print('[' + column + ']', end="")
#     print()

# a = [1, 2, 3, 4, 5]
# b = []

# for i in a:
#     b.append(i * 2)

# print(a)
# print(b) 

# a = [1, 2, 3, 4, 5]
# b = [1 * 2 for i in a]


# print(a)
# print(b) 

# Övningar 

# 1
# numbers_list = []
# numbers_greater_than_10 = 0

# print('Write 10 numbers.')

# for i in range(10):
#     number = float(input(f'Write a number  nr {i + 1}: '))
#     numbers_list.append(number)

#     if number >= 10:
#         numbers_greater_than_10 += 1
    
# print(f'You have written {numbers_greater_than_10} numbers which are equal or greater than 10')

# # 2
# numbers_list = []
# numbers_greater_than_10 = 0
# how_many_wishes = int(input("How many numbers you wanna enter: "))

# for i in range (how_many_wishes):
#     number = float(input(f'Write a number nr {i + 1}: '))
#     numbers_list.append(number)

#     if number >= 10:
#         numbers_greater_than_10 += 1

# print(f'You have written {numbers_greater_than_10} numbers which are equal or greater than 10')

# 3

# numbers_list = []
# print('Write 10 numbers: ')

# for i in range(10):
#     number = float(input(f"write a number nr {i+1}: "))
#     numbers_list.append(number)

# smallest_number = min(numbers_list)
# greatest_number = max(numbers_list)
# mediana = sum(numbers_list)/10

# print(f'You have written {smallest_number} which is the smallest number and {greatest_number} which is the greatest number. the medium number is {mediana}')

# 4
# numbers_list = []
# print('Write 10 numbers: ')
# wish = int(input("How many numbers would you like to pass: "))

# for i in range(wish):
#     number = float(input(f"write a number nr {i+1}: "))
#     numbers_list.append(number)

# smallest_number = min(numbers_list)
# greatest_number = max(numbers_list)
# mediana = sum(numbers_list)/wish

# print(f'You have written {smallest_number} which is the smallest number and {greatest_number} which is the greatest number. the medium number is {mediana}')

# 5
# word = input("write a word: ")
# baklanges_ord = word[::-1]

# print(baklanges_ord)

# 6 and 7 , howmanytaring was 1000 before eerytwhere where needed

# import random
# resultat_lista = [0,0,0,0,0,0]
# howmanytarning = int(input('How many: '))

# for i in range(howmanytarning):
#     kast = random.randint(1,6)
#     resultat_lista[kast-1] += 1

# print(resultat_lista)
# print()
# print('RESULTAT')
# for j in range(6):
#     print(f'{j+1} : {(resultat_lista[j]/howmanytarning) * 100:.2f}%')


# 8

import random
howmanytarning = int(input('How many: '))
howmanysidor = int(input("how many sides shall a tarningen have? "))
resultat_lista = [0] * howmanytarning


for i in range(howmanytarning):
    kast = random.randint(1, howmanysidor)
    resultat_lista[kast-1] += 1

print(resultat_lista)
print()
print('RESULTAT')
for j in range(howmanysidor):
    print(f'{j+1} : {(resultat_lista[j]/howmanytarning) * 100:.2f}%')