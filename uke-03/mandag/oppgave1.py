potetgull = [
    "Kims",
    "Superchips",
    "Sørlandschips",
    "Maarud",
    "Lay's",
    "Pringles",
    "Gårdschips",
    "Totenflak",
]
inp = input("Skriv inn et potetgull-merke\n>")

if inp.capitalize() in potetgull:
    print("Gjenkjent!")
else:
    print(f"Ukjent merke: {inp.capitalize()}")

# Eller

inp = (
    input("Skriv inn et potetgull-merke\n>").lower().split()
)  # gjør alt til lowercase, samt splitter til en liste
inp[0] = inp[0].upper()  # Setter det første tegnet til å være stor
inp = "".join(inp)  # Slår sammen alle elementene i listen til en streng

if inp.capitalize() in potetgull:
    print("Gjenkjent!")
else:
    print(f"Ukjent merke: {inp}")
