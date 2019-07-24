import math

x, y, x1, y1, x2, y2 = map(int, input().split())
distance = None

if x > x1 and x < x2 and y > y2:
    distance = y - y2
elif x > x2 and y > y2:
    distance = math.hypot(x - x2, y - y2)
elif x > x2 and y > y1 and y < y2:
    distance = x - x2
elif x > x2 and y < y1:
    distance = math.hypot(x - x2, y1 - y)
elif x > x1 and x < x2 and y < y1:
    distance = y1 - y
elif x < x1 and y < y1:
    distance = math.hypot(x1 - x, y1 - y)
elif x < x1 and y > y1 and y < y2:
    distance = x1 - x
elif x < x1 and y > y2:
    distance = math.hypot(x1 - x, y - y2)
  
print(distance)