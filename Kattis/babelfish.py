import sys
from collections import defaultdict
dick = dict()
add = True

for line in sys.stdin:
    if add:
        if line == '\n':
            add = False
        else:
            x, y = line.strip().split()
            dick[y] = x
        # print(x, y)
    else:
        # print(query)
        if line.strip() in dick:
            print(dick[line.strip()])
        else:
            print('eh')