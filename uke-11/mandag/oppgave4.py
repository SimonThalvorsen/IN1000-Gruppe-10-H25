class Onske:
    def __init__(self, antall: int, desc:str, min_p:float ):
        self._antall = antall
        self._beskrivelse = desc 
        self._min_pris = min_p

    def passer(self, maksimumspris):
        return self._min_pris <= maksimumspris and self._antall
    
    def valgt(self):
        self._antall -= 1
        return self._beskrivelse
    
    def __str__(self):
        return f"{self._beskrivelse} minPris{self._min_pris} antall gjenstår: {self._antall}"
    

class Onskeliste:
    def __init__(self):
        self._onsker = []

    def nytt_onske(self, ant, min_p, desc):
        onske = Onske(ant, desc, min_p)
        self._onsker.append(onske)

    def hent_onsker(self, max_p):
        out = []
        for onske in self._onsker:
            if onske.passer(max_p):
                out.append(str(onske))
            else:
                out.append("ikke valgbart onske")

        return out

    def onske_oppfylles(self, valg_onske: int):
        return self._onsker[valg_onske].valgt()
    
class Gave:
    def __init__(self, giver, desc):
        self._giver = giver
        self._beskrivelse = desc

    def __str__(self):
        return f"{self._beskrivelse} fra {self._giver}"
    
class Juleferiekalender:
    def __init__(self, ant_dager):
        self._kalender = {}
        for i in range(ant_dager):
            # self._kalender[((24 + i) % 31) + 1] = None
            dag = 25 + i
            if dag > 31:
                dag -= 31
            self._kalender[dag] = None

    def ny_gave(self, dag, desc, giver):
        self._kalender[dag] = Gave(giver, desc)

    def hent_dagens_gave(self, dagnummer):
        maaned = "Desember" if dagnummer > 24 else "Januar"
        
        if dagnummer > 24:
            maaned = "Desember"
        else:
            dagnummer = "Januar"

        dato = f"{dagnummer}.{maaned}"
        gave = self._kalender[dagnummer]
        out = f"Dagens dato: {dato}, dagens gave:\n"
        if gave:
            out += str(gave)
        else:
            out += "Ingen gave idag :("
        return out
    
    def hent_ant_dager(self):
        return len(self._kalender)
    
