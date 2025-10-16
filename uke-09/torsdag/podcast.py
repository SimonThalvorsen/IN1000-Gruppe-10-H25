from episode import Episode

class Podcast:
    def __init__(self, navn: str):
        self._navn = navn
        self._ant_episoder = 0
        self._episoder = []

    def legg_til_episode(self, episodenavn: str, hostnavn: str, gjestenavn: list[str]):
        ep = Episode(episodenavn, self._ant_episoder + 1)
        ep.legg_til_host(hostnavn)
        for gjest in gjestenavn:
            ep.legg_til_gjest(gjest)
        
        self._episoder.append(ep)
        self._ant_episoder += 1

    def skriv_tabell(self):
        print(f"{self._navn} - Antall episoder: {self._ant_episoder}")
        for episode in self._episoder:
            print(episode)

