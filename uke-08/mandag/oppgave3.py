class Barn:
    def __init__(self, ant_foreldre, fdslNr):
        self._ant_foreldre = ant_foreldre
        self._fdslNr = fdslNr


def get_barn(infostreng):
    ant_foreldre, fdslNr = infostreng.split("-")
    return Barn(int(ant_foreldre), fdslNr)

def lst2Barn(lst):
    for i in range(len(lst)):
        lst[i] = get_barn(lst[i])

def main():
    liste = ["VIKLÅRLIG LISTE FRA NAV"]
    lst2Barn(liste)

if __name__== "__main__":
    main()