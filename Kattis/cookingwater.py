N = int(input())
A, B = None, None
for _ in range(N):
    a, b = map(int, input().split())
    
    # starting
    if A == None and B == None:
        A = a 
        B = b 
    
    
    if a > B or b < A:
        print('edward is right')
        quit()
    
    else:
        if a > A:
            A = a 
        if b < B:
            B = b

print('gunilla has a point')