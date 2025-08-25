streng_1 = "A"
streng_2 = "B"
streng_3 = "C"

inp = input("Skriv inn A, B eller C")
inp2 = input("Skriv inn A, B eller C")

if (inp == streng_1 and inp2 == streng_2) or (inp == streng_2 and inp2 == streng_1):
    print(f"Du valgte {inp} og {inp2}")
elif (inp == streng_2 and inp2 == streng_3) or (inp == streng_3 and inp2 == streng_2):
    print(f"Du valgte {inp} og {inp2}")
elif (inp == streng_3 and inp2 == streng_1) or (inp == streng_1 and inp2 == streng_3):
    print(f"Du valgte {inp} og {inp2}")
else:
    print("Ugyldig input")
