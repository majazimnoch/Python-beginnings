# UPPGIFT 1

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

# UPPGIFT 2

weight = int(input("Vad är patientens vikt (kg)? "))
if weight < 20:
    dose = 0.05 * weight
    print(f"Patient skulle äta {str(dose)}mg.")
elif 20 <= weight <= 40:
    dose = 0.1 * weight
    print(f"Patient skulle äta {str(dose)}mg.")
else:
    dose = 0.15 * weight
    print(f"Patient skulle äta {str(dose)}mg.")

