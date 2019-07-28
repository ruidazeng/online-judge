start = int(input())
tracker = dict()
path = [start]

while True:
    tmp_lst = [int(x) for x in input().split()]
    # break if -1
    if tmp_lst[0] == -1: break
    tracker[tmp_lst[0]] = tmp_lst[1::]

while True:
    found = False
    for branch in tracker:
        if start in tracker[branch]:
            start = branch
            path.append(start)
            found = True
            break
    if not found:
        break
    else:
        continue

print(*path)