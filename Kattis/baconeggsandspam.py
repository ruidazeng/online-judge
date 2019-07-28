while True:
    food_tracker = dict()
    n = int(input())
    if n == 0: break
    for _ in range(n):
        lst = [x for x in input().split()]
        for x in lst[1:]:
            if x in food_tracker:
                food_tracker[x].append(lst[0])
            else:
                food_tracker[x] = [lst[0]]
    for x in sorted(food_tracker):
        print(x, end = ' ')
        for y in sorted(food_tracker[x]):
            print(y, end = ' ')
        print()
    
    # space to separate days
    print()