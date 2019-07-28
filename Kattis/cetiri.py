lst = sorted([int(x) for x in input().split()])
diff1 = lst[1] - lst[0]
diff2 = lst[2] - lst[1]

if diff2 > diff1:
    print(lst[1] + diff1)
elif diff1 > diff2:
    print(lst[0] + diff2)
else:
    print(lst[2] + diff1)