def gcd(a, b):
    if b == 0:
        return a 
    else:
        return gcd(b, a % b)

def get_ratio(a, b):
    g = gcd(a, b)
    return '{}/{}'.format(a // g, b // g)

_ = int(input())
rings = [int(x) for x in input().split()]
first = rings[0]

for ring in rings[1:]:
    print(get_ratio(first, ring))