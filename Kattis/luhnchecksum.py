def digit_sum(s):
    return sum([int(char) for char in str(s)])

T = int(input())

for _ in range(T):
    checksum = ''
    luhn = input()
    for c, x in enumerate(luhn[::-1]):
        if c % 2 == 0:
            checksum += x 
        else:
            x = int(x)
            x *= 2
            if x >= 10:
                digit_sum(x)
            checksum += str(x)
    if digit_sum(checksum) % 10 == 0:
        print("PASS")
    else:
        print("FAIL")