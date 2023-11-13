Paris = int(input("Vilken temperatur är det i Paris? "))
Stockholm = int(input("Vilken temperatur är det i Stockholm? "))
difference = Paris - Stockholm
surprise = Stockholm - Paris

if difference > 0 :
    print(f"Det är {str(difference)} grader varmare i Paris än i Stockholm.")
elif difference == 0:
    print(f"Der är lika varmt i Stockholm som Paris, nämligen {str(Paris)} grader.")
else: 
    print(f"Det är {str(surprise)} grader varmare i Stockholm än i Paris.")

# number = float(input('Skriv första tal: '))
# numbertwo = float(input('Skriv andra tal: '))

# if number > numbertwo:
#     print('det första numret är större än den andra')
# else:
#     print('det andra numret är större än den första')
