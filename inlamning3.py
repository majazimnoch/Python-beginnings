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

print(' ::: BILRESAN ::: ')
while True:
    print('My fragar: Ar vi framme snart?')
    svar = input('Du: ')
    if svar == 'ja':
        break
    elif svar == 'nej':
        continue
    elif 'glass' in svar:
        print('my: Horde jag glass?')
        svar = input('du: ')
        if svar == 'ja':
            print('My: jag vill ha glass genast')
            continue
    print('jag ar kissnodig!')
print('My: Vilken tur')