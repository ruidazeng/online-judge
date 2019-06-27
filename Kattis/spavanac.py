h, m = map(int, input().split())

if h - 1 < 0:
    h = 23
    m += 15
    print(h,m)
    
elif m - 45 < 0:
    h -= 1
    m += 15
    print(h, m)
    
else:
    m -= 45
    print(h, m)