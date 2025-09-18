import json

f = open("hotspots", "r")
fileContent = f.read()
f.close()

tilbudListe = json.loads(fileContent)


print(type(tilbudListe))
print(tilbudListe[2]["offer"], sep="\n")
print(tilbudListe[0]["offer"]["heading"])

førsteTilbud = tilbudListe[0]["offer"]
førsteTilbudVareNavn = førsteTilbud["heading"]
førsteTilbudPris = førsteTilbud["pricing"]["price"]

print(f"Varen: {førsteTilbudVareNavn} er på tilbud til {førsteTilbudPris}kr")

# usorterteTilbud = []
#
# for tilbud in tilbudListe:
#     navn = tilbud["offer"]["heading"].capitalize()
#     pris = tilbud["offer"]["pricing"]["price"]
#     pris /= tilbud["offer"]["quantity"]["pieces"]["from"]
#     pre_pris = tilbud["offer"]["pricing"]["pre_price"]
#
#     if pris <= 25:
#         usorterteTilbud.append((navn, pris, pre_pris))
#     # print(f"Varen: {navn} er på tilbud til {pris}kr")
#
# sorterteTilbud = sorted(usorterteTilbud, key=lambda x: x[1])
#
# for tilbud in sorterteTilbud:
#     navn = tilbud[0]
#     pris = tilbud[1]
#     pre_pris = tilbud[2]
#
#     tilbudProsent = "Uvist"
#
#     if pre_pris is not None:
#         tilbudProsent = pre_pris / pris - 1
#
#     print(f"Varen: {navn} er på tilbud til {pris}kr prosent er {tilbudProsent}")
