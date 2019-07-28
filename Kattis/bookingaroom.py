R, C = map(int, input().split())

if R == C:
    print("too late")
else:
    rooms = list(range(1, R + 1))
    for _ in range(C):
        rooms.remove(int(input()))
    print(rooms[0])