def digit_sum(number):
    return sum(map(int, str(number)))
N = int(input())

for _ in range(N):
    n = int(input())
    
    # one less than accordingly 
    digit_sumz = sum(map(int, str(n))) - 1
    
    if digit_sumz == 0:
        print(0)
        continue
    else:
        i = 1
        while True:
            test = digit_sum(n - i)
            if digit_sumz == test:
                print(n - i)
                break
            else:
                i += 1