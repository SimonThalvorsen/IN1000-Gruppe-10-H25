class Bok:
    def __init__(self, sjanger, forfatter, tittel):
        self._sjanger = sjanger
        self._forfatter = forfatter
        self._tittel = tittel

    def hent_sjanger(self):
        return self._sjanger
    
    def hent_forfatter(self):
        return self._forfatter
    
    def hent_tittel(self):
        return self._tittel
    
    ## IKKE PENSUM FØR NESTE UKE !!!!
    def __str__(self):
        return self._tittel
    
    def __repr__(self):
        return self._tittel