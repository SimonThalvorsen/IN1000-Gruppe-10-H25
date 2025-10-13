class Person:
    def __init__(self, fødselsnummer, navn):
        self._fødselsnummer = fødselsnummer
        self._navn = navn

    def hent_fødselsnummer(self):
        return self._fødselsnummer

    def hent_navn(self):
        return self._navn
    def __str__(self):
        return f"{self._navn} ({self._fødselsnummer})"
    
class FdslNr:
    def __init__(self, dato, nr):
        self._dato = dato
        self._nr = nr
        self._fdslsnr = dato+nr
    def __str__(self):
        return self._fdslsnr

class Navn:
    def __init__(self, fnavn, enavn, mnavn):
        self._fnavn = fnavn
        self._enavn = enavn
        self._mnavn = mnavn

    def __str__(self):
        if self._mnavn:
            return f"{self._fnavn} {self._mnavn} {self._enavn}"
        else:
            return f"{self._fnavn} {self._enavn}"

class Par:
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2
        self._par = p1, p2

    def __str__(self):
        return f"{self._p1} ❤️   {self._p2}"


import random
def lag_random_fødselsnummer():
    dato = f"{random.randint(1, 28):02d}{random.randint(1, 12):02d}{random.randint(60, 99)}"
    nr = f"{random.randint(10000, 99999)}"
    return FdslNr(dato, nr)

def lag_random_navn():
    fornavn = random.choice(["Ola", "Kari", "Per", "Lise", "Ali", "Mona", "Henrik", "Anna", "Jonas", "Emma"])
    etternavn = random.choice(["Hansen", "Johansen", "Olsen", "Larsen", "Andersen"])
    mellomnavn = random.choice(["", "Marie", "Alexander", "Elise"])
    return Navn(fornavn, etternavn, mellomnavn)

def lag_random_person():
    fnr = lag_random_fødselsnummer()
    navn = lag_random_navn()
    return Person(fnr, navn)

def main():
    samling = {1:[], 2:[], 3:[], 4:[], 5:[]}

    for etasje in samling:
        for _ in range(5):
            p1 = lag_random_person()
            p2 = lag_random_person()
            par = Par(p1, p2)
            samling[etasje].append(par)

    # Skriv ut innholdet i hver etasje
    for etasje, par_liste in samling.items():
        print(f"\nEtasje {etasje}:")
        for par in par_liste:
            print(" -", par)

if __name__ == "__main__":
    main()