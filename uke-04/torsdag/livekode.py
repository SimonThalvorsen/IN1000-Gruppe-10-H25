def while_loop():
    teller = 0
    sum_kast = 5 # later som denne er tilfeldig
    while (sum_kast <= 10):
        print("Kast nr:", teller, "verdi:", sum_kast)
        teller += 1
        if teller > 10_000_000:
            break

def for_loop():
    print("Starter loop")
    for i in range(10):
        print("Heisann", i)
    print("Avsluttet loop")

def for_each_loop():
    lst = list(range(5)) # [1, 2 ... ,8 ,9]
    print("Starter loop")
    for e in lst:
        print("Heisann", e)
    print("Avsluttet loop")

