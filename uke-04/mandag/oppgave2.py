import random

def print_partall(x):
    tall = []
    for _ in range(x):
        tall.append(random.randint(0,1000))

    for e in tall:
        if not e & 1:
            print(e)  
        elif e % 2 == 0:
            print(e)      

print_partall(10)