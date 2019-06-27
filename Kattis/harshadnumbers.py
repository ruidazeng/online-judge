def hashadNum(num):
    digitSum = sum([int(k) for k in str(num)])
    if num % digitSum == 0:
        return True
    else:
        return False

n = int(input())

while not (hashadNum(n)):
    n += 1 

print(n)