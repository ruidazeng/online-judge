import math
G = 9.8

n = int(input())

for i in range(n):
    v0, theta, x1, h1, h2 = map(float, input().split())
    theta = math.radians(theta)
    t = x1 / (v0 * math.cos(theta))
    y = v0 * t * math.sin(theta) - 0.5 * G * (t ** 2)
    if h1 + 1 <= y <= h2 - 1:
        print("Safe")
    else:
        print("Not Safe")