from bokhylle import Bokhylle
from bok import Bok

class Bibliotek:
    def __init__(self, navn):
        self._navn = navn
        self._bokhylle = Bokhylle("Blindern")

    def boeker_fra_fil(self, filnavn):
        with open("books.csv") as f:
            for linje in f:
                biter = linje.strip().split(",")
                if len(biter) != 8:
                    continue
                bok = Bok([biter[2], biter[3]], biter[1], biter[0])
                self._bokhylle.legg_til_bok(bok)

    def _finn_bok_tittel(self):
        inp = input("Hva heter boken du ser etter?")
        return self._bokhylle.finn_boeker_tittel(inp.lower())
    
    def hent_bok(self):
        boeker = self._finn_bok_tittel()
        for bok in boeker:
            print(bok.hent_tittel())
            inp = input("Vil du låne denne boken? enter for nei, hva som helst for ja")
            if inp:
                return self._bokhylle.ta_ut_bok(bok)