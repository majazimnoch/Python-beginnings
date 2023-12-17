# Ovningar - Funktioner 
# 1,2,3
# def underline(length, dubbel=1):
#     if dubbel==1:
#         print(length*'_')
#     elif dubbel==2:
#         print(length*'=')

# underline(30, 2)

# 4

# def sekunder(dag, timme, minut, sekund):
#     antal_sekunder = sekund+minut*60+timme*60*60+dag*24*60*60
#     return antal_sekunder

# def program():
#     print('Hur manga sekunder: ')

#     dag = int(input('Hur manga dagar? '))
#     timme = int(input('Hur manga timmar? '))
#     minut = int(input('Hur manga minuter? '))
#     sekund = int(input('Hur manga sekunder? '))

#     print(f'Det blir {sekunder(dag, timme, minut, sekund)} sekunder')

# program()

# 5

def moms(pris, procent=25):
    kr = (procent/100)*pris
    return kr
