def da_sort(lst):
    count = 0
    # replica = [x for x in lst]
    result = sorted(array)
    for char in lst:
        if char != result[0]:
            count += 1 
        else:
            result.pop(0)
    return count   
        

T = int(input())

for _ in range(T):
    k, n = map(int, input().split())
    array = []
    if n % 10 == 0:
        iterange = n//10
    else:
        iterange = n//10 + 1
    
    for _ in range(iterange):
        array.extend([int(x) for x in input().split()])
    print(k, da_sort(array))