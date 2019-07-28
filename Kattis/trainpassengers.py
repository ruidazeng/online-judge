C, n = map(int, input().split())

peopleontrain = 0
for i in range(n):
    left, enter, hadtostay = map(int, input().split())
    
    # first station, no one on train.
    if i == 0:
        if left != 0:
            print('impossible')
            quit()
        if peopleontrain != 0:
            print('impossible')
            quit()
    
    peopleontrain -= left
    peopleontrain += enter
    
    if peopleontrain > C:
        print('impossible')
        quit()
    
    # not full
    if peopleontrain < C:
        if hadtostay != 0:
            print('impossible')
            quit()
            
    # last station (no one waiting, empty)
    if i == n - 1:
        if enter != 0:
            print('impossible')
            quit()
        if peopleontrain != 0:
            print('impossible')
            quit()

print('possible')