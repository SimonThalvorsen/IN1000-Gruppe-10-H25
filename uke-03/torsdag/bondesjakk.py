spiller1 = "X"
spiller2 = "O"
turn = True
spillErOver = False
vinner = None

brett = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]


def sjekkVinner():
    global spillErOver
    # Sjekk alle kombinasjoner

    spillErOver = True


def plasser():
    inp = input("Skriv inn koordinat for plassering (x, y)\n>")
    inp = inp.split(",")
    spillertegn = spiller1 if turn else spiller2
    brett[int(inp[0])][int(inp[1])] = spillertegn
    sjekkVinner()


def printBrett():
    print(*brett, sep="\n")


def spill():
    global turn, spillErOver, vinner
    if spillErOver:
        print(f"{vinner} vant spillet!")
    else:
        plasser()
        turn = not turn
    if not spillErOver:
        spill()


spill()
