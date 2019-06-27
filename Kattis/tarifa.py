x = int(input())
n = int(input())

total = 0
for _ in range(n):
    p_i = int(input())
    total += x - p_i

print(x + total)