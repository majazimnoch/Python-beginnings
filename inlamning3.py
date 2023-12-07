# Du ska skriva ett litet spel som heter Gissa summan.
# Spelet går ut på att datorn simulerar tärningskast med två sexsidiga tärningar och sedan
# räknar ut summan av tärningarnas resultat. Sedan får användaren tre försök att gissa
# summan. När användaren har svarat ska hen få feedback om gissningen var för hög eller för
# låg. Om användaren har rätt ges meddelandet: Grattis! Du fick rätt på summan som var
# <summa>. Om användaren inte klarar av att gissa rätt tal på tre försök får hen meddelandet:
# Otur! Du hittade inte summan som var <summa tal>. I svarsmeddelandena ska <summa>
# ersättas med summan av tärningskastet.


# Gra polega na symulacji komputerowej rzutów kostkami dwiema sześciościennymi kostkami, a następnie
# oblicza sumę wyników uzyskanych na kostkach. Następnie użytkownik ma trzy próby odgadnięcia
# Suma. Gdy użytkownik odpowie, powinien otrzymać informację zwrotną, czy odpowiedź była za wysoka, czy za niska
# Niski. Jeśli użytkownik ma rację, pojawia się komunikat: Gratulacje! Dobrze ująłeś tę sumę
# <suma>. Jeśli użytkownikowi nie uda się odgadnąć prawidłowej liczby w trzech próbach, otrzyma komunikat:
# Pech! Nie znalazłeś kwoty, która była <numer sumy>. W wiadomościach odpowiedzi <suma>
# zastąpione sumą rzutu kostką.

import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
sum = dice1 + dice2

for i in range(3):
    guess = int(input("Guess the sum of the two dices: "))

    if guess == sum:
        print(f'Grattis! Du fick rätt på summan som var {sum}')
    elif guess < sum:
        print("För låg. Försök igen")
    else:
        print("För hög. Försök igen")


