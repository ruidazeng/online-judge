import math
def dist(x1, x2, y1, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


while True:
    d, T = input().split()
    d = float(d)
    T = int(T)
    # terminate
    if d == 0.0 and T == 0:
        break
    beehives = []
    sour = 0
    
    for _ in range(T):
        x, y = map(float, input().split())
        beehives.append((x,y))
    
    for x1, y1 in beehives:
        for x2, y2 in beehives:
            # print(dist(x1, x2, y1, y2))
            fuckme = dist(x1, x2, y1, y2)
            if fuckme !=0 and fuckme <= d:
                sour += 1 
                break
    
    print("{0} sour, {1} sweet".format(sour, T - sour))