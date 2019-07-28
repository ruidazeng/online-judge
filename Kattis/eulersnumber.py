N = int(input())
e = 1 # 0! = 1
FACT_ZERO = 1 # 0! = 1
fact = FACT_ZERO

for i in range(1, N + 1):
    # math.factorial led to Time Limit Exceed
    e += 1 / (fact * i)
    fact = fact * i

print(e)