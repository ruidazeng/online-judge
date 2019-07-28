from collections import deque
# list-like container
# fast appends and pops on either end

N = int(input())

for _ in range(N):
    n = int(input())
    d = deque()
    d.append(n)
    for i in range(n-1, 0, -1):
        for _ in range(i):
            d.appendleft(d.pop())
        d.appendleft(i)
        d.appendleft(d.pop())
    print(*d)