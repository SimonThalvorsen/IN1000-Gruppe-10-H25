# Klasser (Klassedefinisjonen)
    # Oppskrift, ikke et objekt
# Innkapsling
    # "pakke inn verdiene"
# Objekt
    # Laget av en oppskrift
# Konstruktør
    #  Det som initialiserer instansen
# Grensesnitt
    # Det man har lov til å gjøre med objektet
# Self?
# Referanse?
# Instans/instansvariabel
# Metode


class Person:
    def __init__(self, navn):
        self._navn = navn
    
    def hent_navn(self) -> str:
        return self._navn
    
    def endre_navn(self, nytt_navn: str) -> None:
        self._navn = nytt_navn





