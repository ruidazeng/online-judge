from array import *
N = int(input())
for i in range(1, N + 1):
    # print test number
    print("Test", i)
    
    m, n = map(int, input().split())
    
    # input array
    T = []
    for _ in range(m):
        T.append(list(input()))
    
    # output array
    P = [[0 for i in range(n)] for j in range(m)]
    
    # mirroring
    for i in range(m):
        for j in range(n):
            P[i][j] = T[m - i - 1][n - j - 1]
     
    # pretty print       
    for i in range(m):
        for j in range(n):
            print(P[i][j], end = '')
        print()