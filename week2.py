# t = float(input('Temp? '))
# if t < 18:
#     print('det är kalt')
#     print('sätt på värmen')
# print(f'Det är {t:.1f} grader')

# d = t1 - t2
# if d < 0:
#     d = -d
# print(f'Tidsskillnad: {d:.2f}')

# pris = float(input('Grundpris? '))
# ålder = int(input('ålder? '))
# if ålder < 12:
#     pris = pris * 0.5
# else:
#     pris = pris * 0.9
# print(f'Pris: {pris:.2f} kr')

# engångspass = 100
# åretskort = 2700
# attendance = int(input('hur många gånger går du till gym per år? '))
# if attendance * 100 < 2700:
#     print ("don't buy the årskort")
# else:
#     print ("buy a yearly kort")

# t = float(input('temp?: '))
# if t < 18:
#     print('zimno')
#     print('ogrzej')
# else:
#     print('cieplo')
#     if t >= 22:
#         print('wystarczajaco cieplo')
# print(f'det är {t:.1f} grader.')

# ÖVNINGAR :

# 1. 
# number = float(input('Skriv ett tal: '))
# if number % 2 == 0:
#     print('numerb is even')
# else:
#     print('number is odd')

# 2. 
# number = float(input('Skriv ett tal: '))
# if number > 0:
#     print('Numret är positivt')
# elif number == 0:
#     print('Numret är 0')
# else:
#     print('numret är negativt')

# 3
# number = float(input('Skriv första tal: '))
# numbertwo = float(input('Skriv andra tal: '))

# if number > numbertwo:
#     print('det första numret är större än den andra')
# else:
#     print('det andra numret är större än den första')

# 4
# number = float(input('Skriv ett jämnt tal: '))
# if number % 2 == 0:
#    print(number)
# else:
#      print(number + 1)

# 5

# import random
# print('Tärningen är kastad')
# n = random.randint(0, 999) 
# print('Du fick ' + str(n) + ' som är ett tvåsuffrigt tal')

# print()
# if tal < 10:
#     print('du gav ', tal, ' som är ett ensiffrigt tal')
# elif tal < 100:
#     print('du gav ', tal, ' som är ett tvåsiffrigt tal')
# else:
#     print('du gav ', tal, ' som är ett tresiffrigt tal')

tal = int(input("type a number between 0-999: "))
print("You have", tal, "which is ", end=" " )

