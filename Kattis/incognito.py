T = int(input())
for _ in range(T):
    options = dict()
    n = int(input())
    for _ in range(n):
        _, typee = input().split()
        options[typee] = options.get(typee, 0) + 1
    
    total = 1
    for typez in options:
        total *= options[typez] + 1 
    
    print(total-1)