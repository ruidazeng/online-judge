import math

while True:
    d, v = map(int, input().split())
    if d == 0 and v == 0:
        break
    
    # Compute the diameter of inner cylinder
    d3 = d**3 - 6*v/math.pi
    d = d3**(1/3)
    
    print(format(d, '.9f'))