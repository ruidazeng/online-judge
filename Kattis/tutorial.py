import math
def complexity(n, i):
    if i == 1:
        if n >= 13:
            return False
        else:
            return math.factorial(n)
    elif i == 2:
        if n >= 30:
            return False
        else:
            return 2**n
    elif i == 3:
        return n**4
    elif i == 4:
        return n**3
    elif i == 5:
        return n**2
    elif i == 6:
        return n * math.log(n,2)
    elif i == 7:
        return n
    else:
        print('Sum Ting Wong')
        
m, n, t = map(int, input().split())
hold = complexity(n, t)

if not hold:
    print('TLE')
elif hold > m:
    print('TLE')
else:
    print('AC')