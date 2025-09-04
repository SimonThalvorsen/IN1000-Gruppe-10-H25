spiller1 = "X"
spiller2 = "O"
turn = True
spillErOver = False
vinner = None

# Selve spillebrettet. Starter med bare "." som betyr tomme ruter
brett = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]


def sjekkVinner():
    # Her brukes "global" for å få tilgang til variablene som ligger utenfor funksjonen.
    # Egentlig er dette litt "juks" og ikke pensum, mer om alternativer for å løse dette kommer i uke 5–6.
    # Uten global ville vi bare laget lokale kopier som ikke påvirker spillet.
    global spillErOver, vinner

    # Rader
    if brett[0][0] == brett[0][1] == brett[0][2] and brett[0][0] != ".":
        spillErOver = True
        vinner = brett[0][0]
    if brett[1][0] == brett[1][1] == brett[1][2] and brett[1][0] != ".":
        spillErOver = True
        vinner = brett[1][0]
    if brett[2][0] == brett[2][1] == brett[2][2] and brett[2][0] != ".":
        spillErOver = True
        vinner = brett[2][0]

    # Kolonner
    if brett[0][0] == brett[1][0] == brett[2][0] and brett[0][0] != ".":
        spillErOver = True
        vinner = brett[0][0]
    if brett[0][1] == brett[1][1] == brett[2][1] and brett[0][1] != ".":
        spillErOver = True
        vinner = brett[0][1]
    if brett[0][2] == brett[1][2] == brett[2][2] and brett[0][2] != ".":
        spillErOver = True
        vinner = brett[0][2]

    # Diagonalene
    if brett[0][0] == brett[1][1] == brett[2][2] and brett[0][0] != ".":
        spillErOver = True
        vinner = brett[0][0]
    if brett[0][2] == brett[1][1] == brett[2][0] and brett[0][2] != ".":
        spillErOver = True
        vinner = brett[0][2]


def plasser():
    # Her bruker vi også global for å kunne endre turn-variabelen utenfor funksjonen
    global turn
    inp = input("Skriv inn koordinat for plassering (x, y)\n>")
    inp = inp.split(",")

    spillertegn = spiller1 if turn else spiller2
    brett[int(inp[0])][int(inp[1])] = spillertegn

    sjekkVinner()
    turn = not turn  # Bytter spiller


def printBrett():
    # Printer brettet rad for rad
    print(brett[0])
    print(brett[1])
    print(brett[2])


def spill():
    global spillErOver, vinner

    if spillErOver:
        printBrett()
        print(f"{vinner} vant spillet!")
    else:
        printBrett()
        plasser()
        # Rekursjon: kaller spill() på nytt så lenge spillet ikke er over
        # Siden vi ikke har lært om løkker enda, så kan vi bruke dette til å "loope" så lenge ingen har vunnet.
        spill()


spill()
