width = int(raw_input())
piece = int(raw_input())
area = 0

for _ in range(piece):
    w, l = map(int, raw_input().split())
    area += w * l 

print int(area/width)