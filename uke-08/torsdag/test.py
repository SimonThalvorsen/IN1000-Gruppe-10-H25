from bibliotek import Bibliotek

def main():
    bib1 = Bibliotek("GS")
    bib1.boeker_fra_fil("books.csv")
    print(bib1._bokhylle._boeker)

    #print(bib1.hent_bok())


if __name__ == "__main__":
    main()