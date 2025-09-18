a = [1, 3, 5, 7, 9]
b = [0, 2, 4, 6, 8]

bord = []

for i in range(len(a)):
    bord.append(a[i])
    bord.append(b[i])

bord = []
while a:
    bord.append(a.pop(0))
    bord.append(b.pop(0))
print(bord)

for i in range(len(bord)-1):
    print(bord[i], bord[i+1])


