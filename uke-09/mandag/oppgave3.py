"""Når innhøstingen av korn og grønnsaker pågår for fullt har bonden ingen traktorer stående på låven. Det vil si at traktorene brukes til arbeid på jordet. Bonden har tre traktorer. Hver traktor har en maksimal trekkvekt (en grense for antall kilo en traktor kan trekke av gangen). Trekkvekten er ulik for hver av de tre traktorene. Fra september til november trengs det gradvis færre traktorer på jordet samtidig. I løpet av september kjører derfor bonden én av traktorene inn på låven. Etter oktober står det to traktorer på låven, og i løpet av november står alle traktorene der. Traktorene kjøres inn på låven i sortert rekkefølge etter maksimal trekkvekt. Oppgaven deres er å lage klasser forbundet med bondens innhøsting, basert på informasjonen over. Dere må finne ut hvilke instansvariabler, metoder og parametere dere trenger selv. Det skal være mulig å hente ut informasjon om traktorene som er på jordet til enhver tid og informasjon om traktorene som står på låven til enhver tid. Vi må kunne finne total trekkvekt som til enhver tid befinner seg på jordet og låven. Lag et hovedprogram som kombinerer objekter av klassene og tilhørende metoder. Hovedprogrammet må oppfylle kravene til funksjonalitet beskrevet i oppgaveteksten.
"""

class Traktor:
    def __init__(self, trekkvekt):
        self._trekkvekt = trekkvekt
        self._i_bruk = True

    def hent_trekkvekt(self):
        return self._trekkvekt

    def status(self):
        return self._i_bruk
    
    def endre_status(self):
        self._i_bruk = not self._i_bruk


class Gård:
    def __init__(self):
        self._låve = []
        self._jordet = []

    def hent_tot_jordet(self):
        sum = 0
        for traktor in self._jordet:
            sum += traktor.hent_trekkvekt()
        return sum
    
    def hent_tot_låve(self):
        sum = 0
        for traktor in self._låve:
            sum += traktor.hent_trekkvekt()
        return sum
    
    def neste_måned(self):
        if not self._jordet: return
        
        cur_min = self._jordet[0]
        for t in self._jordet:
            if t.hent_trekkvekt() < cur_min.hent_trekkvekt():
                cur_min = t
        
        cur_min.endre_status()
        self._jordet.remove(cur_min)
        self._låve.append(cur_min)

    def legg_til_traktor(self, traktor):
        self._jordet.append(traktor)

a = Traktor(10_000)
b = Traktor(15_000)
c = Traktor(20_000)

gård = Gård()
gård.legg_til_traktor(a)
gård.legg_til_traktor(b)
gård.legg_til_traktor(c)
for i in range(4):
    print(f"Tot sum låve: {gård.hent_tot_låve()}")
    print(f"Tot sum jordet: {gård.hent_tot_jordet()}")
    gård.neste_måned()