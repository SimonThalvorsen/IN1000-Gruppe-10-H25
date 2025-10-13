class Rektangel:
    def __init__(self, lengde, bredde):
        self._lengde = lengde
        self._bredde = bredde
        self._bereng_areal()

    def hent_areal(self):
        return self._areal
    
    def _bereng_areal(self):
        self._areal = self._lengde * self._bredde

def main():
    gulv = [(3,3), (5,4), (4,3), (2,4), (2,4)]
    gulvflater = ["kjøkken", "stue", "bad", "sove1", "sove2"]
    objekter = {}
    for i in range(len(gulv)):
        objekter[gulvflater[i]] = Rektangel(gulv[i][0], gulv[i][1])

    sum_areal = 0
    for rom, obj in objekter.items():
        print(f"{rom.capitalize()} har et areal på {obj.hent_areal()}")
        sum_areal += obj.hent_areal()
    print("Totalt gulvareal:", sum_areal)

if __name__ == "__main__":
    main()
