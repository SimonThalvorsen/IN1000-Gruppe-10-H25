from rute import Rute


class Rutenett:
    def __init__(self, x=3, y=3):
        self._rader = x
        self._kol = y
        self._grid = self._fill_grid()
        
    def _fill_grid(self):
        rutenett = []
        for x in range(self._rader):
            rad = []
            for y in range(self._kol):
                rad.append(Rute())
            rutenett.append(rad)
        return rutenett
    
    def plasser_brikke(self, x, y, spiller):
        if -1 < x < self._rader:
            if -1 < y < self._kol:
                if self._grid[x][y].status():
                    self._grid[x][y].plasser_spiller(spiller)
                    return True
        
        print("ikker gyldig plassering") 
        return False  
    
    def sjekk_rutenett(self):
        for rad in self._grid:
            if rad[0].hent_spiller() == rad[1].hent_spiller() == rad[2].hent_spiller():
                if rad[0].hent_spiller() is not None:
                    return rad[0].hent_spiller()
        
        for i in range(3):    
            tmp = []
            for rad in self._grid:
                tmp.append(rad[i].hent_spiller())
            if tmp[0] == tmp[1] == tmp[2]:
                if tmp[0] is not None:
                    return tmp[0]
                
        if self._grid[0][0].hent_spiller() is not None and self._grid[0][0].hent_spiller() == self._grid[1][1].hent_spiller() == self._grid[2][2].hent_spiller():
            return self._grid[0][0].hent_spiller()
        if self._grid[0][2].hent_spiller() is not None and self._grid[0][2].hent_spiller() == self._grid[1][1].hent_spiller() == self._grid[2][0].hent_spiller():
            return self._grid[0][2].hent_spiller()
        
        return False
    
    def display(self):
        for rad in self._grid:
            for rute in rad:
                spiller = rute.hent_spiller()
                if spiller is None:
                    spiller = "."
                print(spiller, end="") 
            print()


def main():
    a = Rutenett()
    print(a._kol)

    
if __name__=="__main__":
    main()