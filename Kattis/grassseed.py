c = float(input())
l = int(input())
area = 0
for x in range(l):
    w_i, l_i = map(float, input().split())
    area += w_i * l_i
area *= c
print(area)