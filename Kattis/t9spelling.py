T = int(input())

d = {}
c = 97
for i in range(2, 8):
    d[c] = (i, 1)
    d[c+1] = (i, 2)
    d[c+2] = (i, 3)
    c += 3
d[c] = (7, 4)
c += 1
for i in range(8, 10):
    d[c] = (i, 1)
    d[c+1] = (i, 2)
    d[c+2] = (i, 3)
    c += 3
d[c] = (9, 4)
d[32] = (0, 1)

for index, _ in enumerate(range(T), 1):
    last = -1
    lis = []
    for j in input():
        t = d[ord(j)]
        if last == t[0]:
            lis += [' ']
        lis += [str(t[0]) * t[1]]
        last = t[0]
    print("Case", "#" + str(index) + ":", "".join(lis))