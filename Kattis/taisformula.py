n = int(input())
t1, v1 = map(float, input().split())
area = 0

for _ in range(n - 1):
    t2, v2 = map(float, input().split())
    area += (t2 - t1) * ((v1 + v2)/2) / 1000
    
    v1 = v2
    t1 = t2

print(area)