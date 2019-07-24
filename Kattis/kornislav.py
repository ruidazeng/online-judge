a, b, c, d = map(int, input().split())

steps = [a, b, c, d]
steps = sorted(steps)

print(steps[0] * steps[2])