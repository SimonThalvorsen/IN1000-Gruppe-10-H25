import random

wins = 0
runs = 1_000_000

for _ in range(runs):
    doors = [1, 0, 0]
    random.shuffle(doors)
    guess = random.randint(0, 2)
    if doors[guess]:
        wins += 1
print(f"NO SWAP\nRuns: {runs}\nWins:{wins}")


wins = 0
runs = 1_000_000

for _ in range(runs):
    doors = [1, 0, 0]
    random.shuffle(doors)
    guess = random.randint(0, 2)
    if not doors[guess]:
        wins += 1
print(f"SWAP\nRuns: {runs}\nWins:{wins}")