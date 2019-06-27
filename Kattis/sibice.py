import math

n, w, h = map(int, input().split())
dgnl = math.sqrt(w**2 + h**2)

for x in range(n):
    if int(input()) <= dgnl:
        print("DA")
    else:
        print("NE")