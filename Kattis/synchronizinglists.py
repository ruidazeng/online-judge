while True:
    n = int(input())
    if n == 0: break
    first = [int(input()) for _ in range(n)]
    second = [int(input()) for _ in range(n)]
    
    output = [None] * n
    
    sorted_second = sorted(second)
    
    for x, n in zip(sorted(first), range(n)):
        output[first.index(x)] = sorted_second[n]
    for x in output:
        print(x)
    print()