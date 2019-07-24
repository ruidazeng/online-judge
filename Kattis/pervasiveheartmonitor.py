import sys
for line in sys.stdin:
    lst = line.split()
    total = 0
    count = 0
    name = list()
    for x in lst:
        try:
            x = float(x)
            total += x
            count += 1
        except:
            name.append(x)
    print(total/count, *name)