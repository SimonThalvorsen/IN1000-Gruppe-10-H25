class Plagg:
    def __init__(self, farger: list[str]):
        self._farger = farger
        self._antall = 0

    def har_farge(self, farge: str):
        return farge in self._farger

    def hent_ant_antrekk(self):
        return self._antall
    
    def oppdater_ant_antrekk(self, endring: int):
        self._antall += endring

    
from random import randint
class Kategori:
    def __init__(self, katNavn: str):
        self._kategori_navn = katNavn
        self._plagg = []

    def nytt_plagg(self, farger: list[str]):
        self._plagg.append(Plagg(farger))

    def finn_plagg_m_farge(self, farge:str):
        out = []
        for p in self._plagg:
            if p.har_farge(farge):
                out.append(p)
        return out

    def trekk_tilfeldig_plagg(self, farge: str):
        plagg_m_farge = self.finn_plagg_m_farge(farge)
        if not plagg_m_farge:
            return None
        
        tall = randint(0, len(plagg_m_farge)-1)
        return plagg_m_farge[tall]
        


class Antrekk:
    def __init__(self, anledning: str, plagg: list[Plagg]):
        self._anledninger = [anledning]
        self._plagg = plagg
        for p in self._plagg:
            p.oppdater_ant_antrekk(1)

    def hent_plaggene(self):
        return self._plagg
    
    def legg_til_anledning(self, anledning: str):
        self._anledninger.append(anledning)

    def passer_til(self, anledning: str):
        return anledning in self._anledninger
    
    def har_farge(self, farge: str):
        for p in self._plagg:
            if p.har_farge(farge):
                return True
        return False

class Gardrobe:
    def __init__(self):
        self._kategorier = {}
        self._antrekk = []

    def nytt_plagg(self, katNavn: str, farger: list[str]):
        if katNavn in self._kategorier:
            self._kategorier[katNavn].nytt_plagg(farger)
        else:
            self._kategorier[katNavn] = Kategori(katNavn)
            self._kategorier[katNavn].nytt_plagg(farger)

    def finn_antrekk_til_anledning(self, anledning: str):
        out = []
        for a in self._antrekk:
            if a.passer_til_anledning(anledning):
                out.append(a)
        return out
    
    def velg_forste_antrekk(self, anledning: str, farge: str):
        antrekk_som_passer = self.finn_antrekk_til_anledning(anledning)
        for a in antrekk_som_passer:
            if a.har_farge(farge):
                return a
        return None
    
    def finn_plagg_til_antrekk(self, kategNavn: list[str], farge:str):
        out = []
        for kat in kategNavn:
            if kat in self._kategorier:
                out.append(self._kategorier[kat].trekk_tilfeldig_plagg(farge))
            else:
                out.append(None)
        # antar den skal returner enten et fullverdig antrekk eller None, 
        # dvs [plagg1, plagg2, None, plagg4] -> None
        if None in out:
            return None
        return out
    
    def lag_nytt_antrekk(self, katNavn: list[str], farge: str, anledning: str):
        lstPlagg = self.finn_plagg_til_antrekk(katNavn, farge)
        if lstPlagg is None:
            return False
        
        antrekk = Antrekk(anledning, lstPlagg)
        self._antrekk.append(antrekk)
        return True



