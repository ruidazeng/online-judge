T = int(input())

for _ in range(T):
    _, _ = map(int, input().split())
    day = 0 # first friday on the 6th day, sunday on the 1st day
    fridayz = 0
    days_in_months = [int(x) for x in input().split()]
    for dim in days_in_months:
        for date in range(1, dim + 1):
            day += 1
            #print(day)
            if date == 13 and day % 7 == 6:
                fridayz += 1
    
    print(fridayz)