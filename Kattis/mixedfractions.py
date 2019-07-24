while True:
    numer, denom = map(int, input().split())
    if numer == 0 and denom == 0:
        break
    else:
        integer = numer // denom
        newNumer = numer % denom
        newDenom = denom
        print(integer, newNumer, '/', newDenom)