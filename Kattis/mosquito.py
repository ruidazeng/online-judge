import sys
for line in sys.stdin:
    M, P, L, E, R, S, N = map(int, line.split())
    for week in range(N):
        new_larva = M * E 
        new_pupa = L//R
        new_mosquito = P//S
        M = new_mosquito
        L = new_larva
        P = new_pupa
    print(M)