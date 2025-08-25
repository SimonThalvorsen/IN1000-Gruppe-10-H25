streng_1 = "A"
streng_2 = "B"
streng_3 = "C"

inp = input("Skriv inn A, B eller C")

# if inp in [streng_1, streng_2, streng_3]:
#     print(inp)
# else:
#     print("Fant ikke strengen")

if inp == streng_1:
    print("Du skrev inn streng 1")
elif inp == streng_2:
    print(streng_2)
...


if inp == streng_1 or inp == streng_2 or inp == streng_3:
    print(inp)
else:
    print("Fant ikke strengen")
