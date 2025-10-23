from rutenett import Rutenett
def main():
    rn = Rutenett()
    rn.display()
    p1 = "X"
    p2 = "O"
    spiller1_tur = True

    while not rn.sjekk_rutenett():
        if spiller1_tur:
            spiller = p1
        else:
            spiller = p2
        rn.display()
        inp = input(f"SPILLER {spiller} sin tur, SKRIV INN PLASSERING X,Y").split(",")
        x, y = int(inp[0]), int(inp[1])
        
        rn.plasser_brikke(x,y,spiller)
        spiller1_tur = not spiller1_tur

    print(f"Spiller {rn.sjekk_rutenett()} vant!!! Gratulerer")

if __name__=="__main__":
    main()