from bok import Bok

class Bokhylle:
    def __init__(self, plassering: str):
        self._plassering = plassering
        self._boeker = []

    def legg_til_bok(self, bok: Bok):
        self._boeker.append(bok)
    
    def ta_ut_bok(self, bok: Bok):
        if bok in self._boeker:
            self._boeker.remove(bok)
        return bok

    def finn_boeker_tittel(self, tittel: str):
        ret = []
        for bok in self._boeker:
            if tittel in bok.hent_tittel().lower():
                ret.append(bok)
        return ret
    
    def finn_boeker_sjanger(self, sjanger: str):
        ret = []
        for bok in self._boeker:
            if sjanger in bok.hent_sjanger().lower():
                ret.append(bok)
        return ret
    
    def finn_boeker_forfatter(self, forfatter: str):
        ret = []
        for bok in self._boeker:
            if forfatter in bok.hent_forfatter().lower():
                ret.append(bok)
        return ret

        