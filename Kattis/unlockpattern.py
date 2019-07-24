def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

order = [None] * 9
for i in range(3):
    for j, n in enumerate(map(int, input().split())):
        order[n - 1] = (i, j)
print(sum(distance(a, b) for a, b in zip(order, order[1:])))