bruker = {"1234.1234.1234.1234": 1000, "1111.2222.3333.4444": 100000000}
cur_konto = [""]

def sett_inn():
    gammel = bruker[cur_konto[0]]
    bruker[cur_konto[0]] += int(input("Hvor mye vil du sette inn?\n>"))
    print(f"Ny saldo: {bruker[cur_konto[0]]}\nGammel saldo:{gammel}")

def sjekk_saldo():
    print(f"Kontonr. {cur_konto[0]}")
    print("Saldo:", bruker[cur_konto[0]])

def ta_ut():
    sjekk_saldo()
    gammel = bruker[cur_konto[0]]
    inp = int(input("Hvor mye vil du ta ut?\n>"))
    if inp > bruker[cur_konto[0]]:
        print("Du har ikke nok penger på konto!")
        print(f"Saldo: {gammel}")
        print(f"Forsøkt uttak: {inp}")
    else:
        bruker[cur_konto[0]] -= inp
        print(f"Ny saldo: {bruker[cur_konto[0]]}\nGammel saldo:{gammel}")

def kommandoer():
    print("Velkommen til ABC-bank! \n\
    Tast:\n\
        1 - For å sjekke saldo,\n\
        2 - For uttak,\n\
        3 - For innskudd, \n\
        x - For å avslutte.")

def meny():
    inp = input("Skriv inn kontonr\n>")
    cur_konto[0] = inp
    inp = input(">")
    if inp == "1":
        sjekk_saldo()
        meny()

    elif inp == "2":
        ta_ut()
        meny()
    elif inp == "3":
        sett_inn()
        meny()
    elif inp != "x":
        print("Ukjent kommando, prøver igjen\n")
        kommandoer()
        meny()
    else:
        print("Ha en fin dag videre!")

kommandoer()
meny()