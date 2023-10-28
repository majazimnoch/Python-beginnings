# def school_age_calculator(age, name):
#     if age < 4:
#         print("Enjoy your time.", name, "is only", age)
#     elif age == 5:
#         print("Enjoy kindergarten,", name)
#     else:
#         print("they grow up so fast!")

# school_age_calculator(3, "Thomas")

# def add_ten_to_age(age):
#     new_age = age + 10
#     return new_age

# How_Old_Will_I_Be = add_ten_to_age(3)
# print(How_Old_Will_I_Be)

#while
# x=0
# while (x<5):
#     print(x)
#     x=x+1

# #For
# for x in range(5,10):
#     print(x)
# days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# # for d in days:
# #     if(d=="Thu"):break
# #     print(d)

# # for d in days:
# #     if(d=="Thu"):continue
# #     print(d)

# import math
# print("pi is", math.pi)

# namn = 'Ida'
# print ('Hej', namn)

# print(6/3)

# print("Hej")

# namn = input("Vad heter du")
# print("Hej", namn)

# name = 'Maja'
# surname = 'Lund'

# sentence = f'My name is {name} {surname}'
# print(sentence)

# import math
# print(float(4))

# import math
# print(int(4.6))

# # Övningar - input och output v2

# 1

# name = "Maja"
# surname = "Zimnoch"

# print(name)
# print(surname)

# print(name + " " + surname)
# print("Förnamn: " + name + ", Efternamn: " + surname)

# output: Förnamn: Maja, Efternamn: Zimnoch

# 2

# name = "Cherilyn"
# nickname = '"Cher"'
# surname = "Sarkisian"

# print (name + " " + nickname + " " + surname + " ")

# output: Cherilyn "Cher" Sarkisian 

# 3
# print("För att radbryta text skriver man \\n där radbrytningen ska ske")


# output: För att radbryta text skriver man \n där radbrytningen ska ske

# 4

# name = input("Vad heter du")
# print("Hej " + name + ", roligt att du kommit hit")

# 5

# name = input("Vad heter du i förnamn: ")
# surname = input("Vad hete du i efternamn: ")

# print(name+"."+surname+"@"+"gmail.com")

#6
# x = 12
# y = 12 * 12
# print(x, "i kvadrat blir", y )

#7

# x = 73
# y = 23
# print(round(x/y, 2))
# print(x/y)

# 8

# farenheit = 80
# celcius = 80/27
# print(celcius)

# farenheit = float(input('write a number in farenheit: '))
# celcius = (farenheit - 32) * 5/9
# print(celcius)

# name = "Maja"
# print(f"Hej {name}.Vad kull att du ha börjat programmera.")
# print("Hej {name}.Vad kull att du ha börjat programmera.")

# svar = input('Skriv ett tal: ')
# x = float(svar)
# y = x * x
# print(f'Talet i kvadrat är {y:2f}')

# print(f'Talet i kvadrat är {y:9.2f}')

# z = 1.666
# print(f'Resultat:{z:06.2f}')

# i = 19
# print(f'Resultat:{i}')

# j = 107
# print(f'Resultat:{j:4}')

# k = 4
# print(f'Resultat:{k:03}')
# i = 13
# j = 2
# print(i + 3 * j)

# print(16 // 5)
# print(13 % 5)
# print(5 ** 3)


# import random
# print('Tärningen är kastad')
# n = random.randint(1,8) # ett slumtal mellan 1 och 8-
# print('Du fick', n)

# l = int(input("Skriv en längd: "))
# b = int(input("Skriv en bredd: "))
# d = int(input("Skriv en djup: "))

# print("Volymen är", (l*b*d))


# sek = int(input("Ange antalet kronor du vill växla: "))
# euro = sek / 9.82
# print(f"{sek} SEK ger {euro:.2f}) euro")

# uppgift 1
# # name = input("Vad heter du? ")
# print("Hej " + name + "!" + " Vad kul att du är här.")

# output:
# Vad heter du? Maja
# Hej Maja! Vad kul att du är här.

# age = int(input("Hur gammal är du? "))
# future = age + 4
# print(name + ", om fyra år är du " + str(age + 3) + " år gammal.")
# or 
# print(name + ", om fyra år är du " + str(future) + " år gammal.")

# uppgift 2

number = int(input("Skriv ett heltal: "))
number_two = int(input("Skriv ett heltal till: "))
sum = number + number_two
difference = number - number_two
print(f"Summan av talen är {str(sum)}")
print(f"Differensen av talen är {str(difference)}")
      
# print(f"Hej {name}.Vad kull att du ha börjat programmera.")