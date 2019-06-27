total = 0
N = int(input())

for _ in range(N):
    a, b = map(float, input().split())
    total += a * b

print(total)