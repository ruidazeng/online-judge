n = int(input())

for i in range(n):
    _ = int(input())
    guests = [int(x) for x in input().split()]
    for guest in guests:
        if guests.count(guest) == 1:
            alone = guest
            break
    print("Case #{}: {}".format(i + 1, alone)) 