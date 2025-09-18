# Oppgave 5
# Anta at du har filen “historiske_personer.txt”.
#
# A) Les inn alle linjene og lagre dem i en liste. Første historiske person (linje) i filen skal ligge først i lista, o.s.v. 
# Tips: husk å åpne og lukke filen.
#
# B) Opprett filen “historiske_personer.txt”. Fyll den med noen historiske personer ved å skrive direkte i fila. Legg fila i samme mappe som .py-filen din.
#
# C) Test at programmet fra a) fungerer ved å bruke filen du opprettet i b).

f = open("historiske_personer.txt", "r")

# for linje in f:
#     print(linje.strip("\n"))
    
linjer = f.readlines()
print(linjer)
for x in linjer:
    print(x.strip("\n"))

# linjer.sort()
# sorted(linjer) -> ['aaaaa\n', 'b\n', 'c\n', 'd\n', 'e\n', 'f\n', 'g\n', 'i\n', 'k\n', 'l\n', 'x\n', 'y\n', 'z\n']
# linjer = sorted(linjer)
# print(linjer)

f.close()

#
# Oppgave 6
# Lag et program som skriver historiske personers navn og fødselsår til fil. Navnene og fødselsårene skal være lagret i en ordbok,
# med navn som nøkler og fødselsår som verdier.
# Tips: husk å åpne og lukke filen ved behov.
#
# Opprett en ordbok med fem historiske personer og deres fødselsår.
#
# Skriv navn og fødselsår til fil. Hver linje skal ha en historisk persons navn og fødselsår, atskilt med ; (semikolon). 
# Filen skal hete “historiske_personer_fodt.txt”. 
#
# Lag et nytt program, som bruker en funksjon til å lese inn filen du laget i b) og som returnerer en ordbok tilsvarende den i a). 
# Funksjonen skal ha parameter filnavn. 

ordbok = {"Simon": 2002, "Shane West": 1978, "Harry Muskee": 1941}
f = open("historiske_personer.txt", "w")

for key in ordbok:
    val = ordbok[key]
    f.write(key)
    f.write(";")
    f.write(str(val))
    f.write("\n")

f.close()

