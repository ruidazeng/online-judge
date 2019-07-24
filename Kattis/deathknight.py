N = int(input())
victoire = 0

for _ in range(N):
    moves = input()
    if "CD" not in moves:
        victoire += 1

print(victoire)