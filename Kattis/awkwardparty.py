from collections import defaultdict

n = int(input())
a = [int(x) for x in input().split()]
ans = n
last = defaultdict(lambda: -n)
for i, x in enumerate(a):
    ans = min(ans, i - last[x])
    last[x] = i

print(ans)