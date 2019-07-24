p = int(input())

for _ in range(p):
    k, n = map(int, input().split())

    n_even = n * (n + 1)
    n_pos = n_even // 2
    n_odd = n_even - n
    
    print(k, n_pos, n_odd, n_even)