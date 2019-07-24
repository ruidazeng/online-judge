A, B, C = map(int, input().split())
money = 0

start1, end1 = map(int, input().split())
truck1 = list(range(start1, end1))
start2, end2 = map(int, input().split())
truck2 = list(range(start2, end2))
start3, end3 = map(int, input().split())
truck3 = list(range(start3, end3))

for i in range(min(start1, start2, start3), max(end1, end2, end3)):
    if (i in truck1) and (i in truck2) and (i in truck3):
        money += 3 * C
    elif (
            (i in truck1) and (i in truck2)
        or (i in truck3) and (i in truck2)
        or (i in truck1) and (i in truck3)
        ):
        money += 2 * B
    elif (i in truck1) or (i in truck2) or (i in truck3):
        money += A

print(money)