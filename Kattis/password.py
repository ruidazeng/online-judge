tries = 0
T = int(input())
lst = list()
for _ in range(T):
    lst.append(input().split()[1])
for i, x in enumerate(sorted(lst)[::-1]):
    tries += float(x) * (i + 1)

print(tries)