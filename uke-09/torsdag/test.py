from podcast import Podcast 

def main():
    pod = Podcast("Abels tårn")
    navn = "Forskningsfronten - Kreativitet kan gjøre hjernen sju år yngre"
    host = "Torkild Jemterud"
    gjester = ["meg", "deg", "han der"]
    pod.legg_til_episode(navn, host, gjester)
    navn = "Forskningsfronten - del 2"
    pod.legg_til_episode(navn, host, gjester)

    pod.skriv_tabell()




if __name__ == "__main__":
    main()