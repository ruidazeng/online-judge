_, T = map(int, input().split())

times = [int(x) for x in input().split()]

sum = 0
count = 0

for t in times:
    if sum + t <= T:
        sum += t  
        count += 1
    else:
        break
        
print(count)