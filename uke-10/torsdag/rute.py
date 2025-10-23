class Rute:
    def __init__(self):
        self._status = True
        self._spiller = None

    def hent_spiller(self):
        return self._spiller
    
    def status(self):
        return self._status
    
    def plasser_spiller(self, spiller):
        self._spiller = spiller
        self._status = False


def main():
    a = Rute()
    A = "X"
    B = "O"
    print(a.status())
    print(a.status())
    print(a.status())
    if a.status():
        a.plasser_spiller(A)
    print(a.status())
    print(a.hent_spiller())
    if a.status():
        a.plasser_spiller(B)
    print(a.hent_spiller())

    
if __name__=="__main__":
    main()