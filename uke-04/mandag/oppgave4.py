varer = ["a", "a", "a", "b", "c"]

ordbok = {}

for vare in varer:
    if vare in ordbok:
        ordbok[vare] += 1
    else:
        ordbok[vare] = 1

print(ordbok)
print(sorted(ordbok.keys(), reverse=True))


# varer.sort()
# sorted(varer)