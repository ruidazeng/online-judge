import sys

case = 1
for line in sys.stdin:
    lst = [int(x) for x in line.split()][1:]
    print("Case", str(case) + ":", min(lst), max(lst), max(lst) - min(lst))
    case += 1