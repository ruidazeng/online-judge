n = int(input())
days = 0

for x in [int(x) for x in input().split()]:
    if x < 0:
        days += 1 
        
print(days)