P = int(input())

for _ in range(P):
    k, n = map(int, input().split())
    print(k, int(((n + 1) * n) / 2 + n))