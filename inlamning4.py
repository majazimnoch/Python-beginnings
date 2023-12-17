# # 1
def skrivOrd(ordet):
    for i in range(len(ordet)):
        print(ordet)

valtOrd = input("Write a word: ")
skrivOrd(valtOrd)

# # 2

def skrivOrd(ordet):
    for i in range(1, len(ordet) + 1):
        print(f'{i}. {ordet}')

valtOrd = input("Write a word: ")

skrivOrd(valtOrd)

# # 3 and 4

def FindGreatestNumber(a, b, c):
    GreatestNumber = a

    if b > GreatestNumber:
        GreatestNumber = b

    if c > GreatestNumber:
        GreatestNumber = c

    return GreatestNumber

a = 7888
b = 89
c = 9

Greatest = FindGreatestNumber(a, b, c)

print("The greater number is: ", Greatest)