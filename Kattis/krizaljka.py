A, B = input().split()

# Find the index of the first letter from str1 that is in str2.
for char1 in A:
    find = False
    for char2 in B:
        if char1 == char2:
            index1 = A.index(char1)
            index2 = B.index(char2)
            # break out of nested for loop
            find = True
    if find:
        break

# Print as formatted
for i in range(len(B)):
    if i == index2:
        print(A, end='')
    else:
        for j in range(len(A)):
            if j == index1:
                print(B[i],end='')
            else:
                print('.',end='')
    print()