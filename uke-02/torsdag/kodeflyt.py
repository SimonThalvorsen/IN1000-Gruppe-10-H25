def prosedyre1(): # 1
    print("Hei fra prosedyre1")
    prosedyre2()

def prosedyre2(): # 2
    tall = int(input("Skriv inn et tall\n>"))
    if tall % 2:
        prosedyre1()
    else:
        prosedyre3()

def prosedyre3(): # 3
    tall = int(input("Skriv inn et tall\n>"))
    if tall > 10:
        prosedyre1()

prosedyre1() # 4
