from __future__ import annotations # Ikke tenke for mye på denne
from person import Person


class Episode:
    def __init__(self, tittel: str, nummer: int):
        self._tittel = tittel
        self._nummer = nummer
        self._host = None
        self._gjester = []

    def legg_til_host(self, navn: str):
        if self._host is None:  
            self._host = Person(navn, "Host")

    def legg_til_gjest(self, navn: str):
        self._gjester.append(Person(navn, "Gjest"))
        
    def __str__(self):
        out = ""
        out += f"Tittel:{self._tittel} - nr:{self._nummer}\n  Hosted by: {self._host}\n"
        for gjest in self._gjester:
            out += "\t" + str(gjest) + "\n"
        return out
    
    def __eq__(self, other: Episode):
        return self._host == other._host
    