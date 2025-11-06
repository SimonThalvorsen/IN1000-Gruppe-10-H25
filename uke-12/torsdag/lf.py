def points(streng: str):
    return len(streng) if streng != "lyn" else 0

def poengsum(lst: list[str]):
    psum = 0
    for ord in lst:
        psum += points(ord)
    return psum

    # return sum(map(points,lst))

def velg(lst: list):
    inp = int(input())

    while inp not in range(len(lst)):
        inp = int(input())

    return lst[inp]

def spill_et_kort(kortliste: list[list[str]]):
    """
    valgt_kort = velg(kortliste)
    psum = poengsum(valgt_kort)
    print("Du fikk:", psum, "poeng!)
    """
    print(poengsum(velg(kortliste)))

def prosedyre(setning):
    tell_ord = {}
    for ord in setning:
        if ord not in tell_ord:
            tell_ord[ord] = 0
        tell_ord[ord] += 1
    for ord in tell_ord:
        print("Antall", ord, ":", tell_ord[ord])
    
prosedyre(["F", "E", "R", "S", "K", "E", "N", "B", "R", "U", "S"])
prosedyre( ["Flodhest", "er", "best", "ingen", "protest"])

def simple(setning):
    for ord in set(setning):
        print("Antall", ord, ":", setning.count(ord))

def gloomhaven_a(nummer, oppdrag):
    blocker = oppdrag[nummer][1]
    for e in blocker:
        if oppdrag[e][0]:
            return True
    return False

def gloomhaven_b(nummer, oppdrag):
    if nummer not in oppdrag or gloomhaven_a(nummer, oppdrag):
        return False 
    
    for e in oppdrag[nummer][2]:
        if not oppdrag[e][0]:
            return False

    return True