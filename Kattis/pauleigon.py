from math import ceil

N, P, Q = map(int, input().split())

rounds = P + Q + 1

if ceil(rounds/N) % 2 == 0:
    print("opponent")
else:
    print("paul")