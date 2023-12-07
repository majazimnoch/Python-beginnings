# Övning 1

# import random

# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# dice_sum = dice1 + dice2
# guess_number = 0

# for i in range(3):
#     guess = int(input("Gissa summan av tärningarna (2-12): "))
#     guess_number += 1

#     if guess == dice_sum:
#         print(f'Grattis! Du fick rätt på summan som var {dice_sum} och du försökt {guess_number} gånger')
#         break
#     elif guess < dice_sum:
#         print("För låg. Försök igen")
#     else:
#         print("För hög. Försök igen")
# print(f'Otur! Du hittade inte summan som var {dice_sum} och du försökt {guess_number} gånger.')


import random
while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    guess_number = 0

    for i in range(3):
        guess = int(input("Gissa summan av tärningarna (2-12): "))
        guess_number += 1

        if guess == dice_sum:
            print(f'Grattis! Du fick rätt på summan som var {dice_sum} och du försökt {guess_number} gånger')
            break
        elif guess < dice_sum:
            print("För låg. Försök igen")
        else:
            print("För hög. Försök igen")
    print(f'Otur! Du hittade inte summan som var {dice_sum} och du försökt {guess_number} gånger.')

    play_again = input("Önskar du att spela igen? Skriv ja eller nej: ")

    if play_again != 'ja':
        break

    print("\nNytt spel börjar...\n")



