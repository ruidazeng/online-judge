from math import degrees, atan

while True:
    a, b, s, m, n = map(int, input().split())
    if a == 0 and b == 0 and s == 0 and m == 0 and n == 0:
        break
    
    # tan = opposite / ajacent (hypotenuse)
    angle = degrees(atan((b * n) / (a * m)))
    
    # Magnitude or norm (treat as directional vectors)
    dist = ((b * n) ** 2 + (a * m) ** 2) ** 0.5
    veloct = dist / s
    print("{:.2f} {:.2f}".format(angle, veloct))