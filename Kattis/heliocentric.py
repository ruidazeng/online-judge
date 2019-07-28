import sys

case = 0
EARTH = 365
MARS = 687

for line in sys.stdin:
    day = 0
    case += 1
    e, m = map(int, line.split())
    while True:
        if e == 0 and m == 0:
            print("Case", str(case) + ":", day)
            break
        else:
            e += 1 
            m += 1
            if e == EARTH:
                e = 0
            if m == MARS:
                m = 0
            
            day += 1