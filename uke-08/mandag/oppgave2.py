class Gruppe:
    def __init__(self, grNr):
        self._oppmote = []
        self._grNr = grNr
        self._totOppmote = 0

    def registrer_oppmote(self, oppmote):
        self._oppmote.append(oppmote)
        self._totOppmote += oppmote

    def get_oppmote(self):
        return self._totOppmote

    def hent_nr(self):
        return self._grNr
    

def main():
    fil = open("oppmøte_in1000.txt", "r")

    grupper = []
    l1 = fil.readline().strip().split(";")
    for gruppe in l1:
        grupper.append(Gruppe(gruppe))
    for line in fil:
        bits = line.strip().split(";")
        for i in range(len(bits)):
            grupper[i].registrer_oppmote(int(bits[i]))
    fil.close()

    tot_oppmotte = 0
    for gruppe in grupper:
        print(f"{gruppe.hent_nr()}, totalt oppmøte: {gruppe.get_oppmote()}")
        tot_oppmotte += gruppe.get_oppmote()
    
    print(tot_oppmotte)

if __name__ == "__main__":
    main()


    