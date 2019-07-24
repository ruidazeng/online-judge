_, Q = map(int, input().split())
companies = [int(x) for x in input().split()]

for _ in range(Q):
    indicator, x, y = map(int, input().split())
    if indicator == 1:
        companies[x-1] = y
    elif indicator == 2:
        print(abs(companies[x-1] - companies[y-1]))