def digit_sum(s):
    return sum([int(x) for x in str(s)])
    
    
while True:
    n = int(input())
    if n == 0:
        break
    p = 11 # p is bigger than 10.
    while True:
        if digit_sum(n) == digit_sum(n * p):
            print(p)
            break
        else:
            p += 1