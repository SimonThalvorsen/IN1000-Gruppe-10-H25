a = [0, 0, 0, 0, 0] # []
b = [1, 0, 2, 0, 3] # [1, 0, 2, 0, 3]
c = [0, 0, 1, 2, 0, 3, 0, 0, 4, 0] # [1, 2, 0, 3, 0, 0,4]

def fjern_null(liste):
    while liste and liste[0] == 0:
        liste.pop(0)
    while liste and liste[-1] == 0:
        liste.pop(-1)

fjern_null(a)
print(a)
fjern_null(b)
print(b)
fjern_null(c)
print(c)