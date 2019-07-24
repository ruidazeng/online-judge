N = int(input())
before = input()
after = input()

if N % 2 == 0:
    print("Deletion succeeded" if before == after else "Deletion failed")
else:
    find = True
    for i in range(len(before)):
        if before[i] == after[i]:
            find = False
            break
    print("Deletion succeeded" if find else "Deletion failed")