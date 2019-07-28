import sys
from math import floor

def get_divisors(n):
    div = [1]
    # Only iterates "half" way through (in terms of multiplication)
    for i in range(2, 1 + int(floor(n ** 0.5))):
        if n % i == 0:
            div.append(i)
            div.append(n // i)
    # Remove duplicates by turning Python list into set
    return set(div)

    
for num in sys.stdin.readlines():
    num = int(num)
    div_sum = sum(get_divisors(num))
    if num == div_sum:
        print(num, "perfect")
    elif abs(num - div_sum) <= 2:
        print(num, "almost perfect")
    else:
        print(num, "not perfect")