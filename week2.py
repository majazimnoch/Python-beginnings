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

t = float(input('temp?: '))
if t < 18:
    print('zimno')
    print('ogrzej')
else:
    print('cieplo')
    if t >= 22:
        print('wystarczajaco cieplo')
print(f'det är {t:.1f} grader.')