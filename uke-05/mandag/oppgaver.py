def badminton(per_vil, palle_vil, espen_vil):
    lst = [per_vil, palle_vil, espen_vil]
    teller = 0
    for e in lst:
        if e:
            teller += 1
    if teller == 2:
        return True
    else: 
        return False
    
def badminton2(per_vil, palle_vil, espen_vil):
    return per_vil + palle_vil + espen_vil == 2


def summer_rabatt(vareliste, førpris, nypris):
    tot_rabatt = 0
    for vare in vareliste:
        tot_rabatt += førpris[vare] - nypris[vare]

    return tot_rabatt

def heie(tabellplass_ordbok):
    if tabellplass_ordbok["Brann"] <= 3:
        return "Brann"
    for lag in tabellplass_ordbok:
        if tabellplass_ordbok[lag] == 1:
            return lag

def oppmoete(filnavn):
    f = open(filnavn, "r")
    lst = []
    for linje in f:
        a = linje.split(";")
        lst.append(a)

    grupper = lst.pop(0)
    uke11 = lst[10]
    for i in range(len(uke11)):
        if int(uke11[i]) >= 20:
            print("Fant en gruppe,", grupper[i])

def karantene(vaksinert, farge):
    if vaksinert:
        return 0
    """if farge == "Grønn":
        return 3
    else:
        return 10"""
    return 3 if farge == "Grønn" else 10


def lag_interessegrupper(personers_interesse):
    ret = {}

    for navn, interesse in personers_interesse.items():
        if interesse in ret:
            ret[interesse].append(navn)
        else:
            ret[interesse] = [navn]
    return ret

[["Spania", "Frankrike"], ["Frankrike", "Norge"]] # True
[["Russland", "Tyskland"], ["Tyskland","Sverige"], ["Norge", "Belgia"]] # False
def sjekk_reise(reise):
    prev = reise[0][0]
    for reiserute in reise:
        if reiserute[0] != prev:
            return False
        prev = reiserute[1]
    return True

def sjekk_reise2(reise):
    for i in range(len(reise) - 1):
        if reise[i][1] != reise[i+1][0]:
            return False
    return True