E, F, C = map(int, input().split())

bottles = E + F 
drank = 0

while bottles >= C:
    # while he still has enough empty bottles to purchase more 
    
    bottles -= C - 1 # used F empty bottles to buy 1
    drank += 1

print(drank)