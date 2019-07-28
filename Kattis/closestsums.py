import sys
kase = 0

# O(N), the pair with sum closest to x 
def find_pair(arr, n, x):
    # n = len(arr)
    MAX_VAL = 10e9
    
    # To store indexes of result pair 
    res_l, res_r = 0, 0
      
    #Initialize left and right indexes 
    # and difference between 
    # pair sum and x 
    l, r, diff = 0, n-1, MAX_VAL
      
    # While there are elements between l and r 
    while r > l: 
        # Check if this pair is closer than the  
        # closest pair so far 
        if abs(arr[l] + arr[r] - x) < abs(diff): 
            res_l = l 
            res_r = r 
            diff = abs(arr[l] + arr[r] - x) 
      
        if arr[l] + arr[r] > x: 
        # If this pair has more sum, move to  
        # smaller values. 
            r -= 1
        else: 
        # Move to larger values 
            l += 1
    
    ans = arr[res_l] + arr[res_r]  
    return ans
    
    
for line in sys.stdin:
    kase += 1 
    print('Case {0}:'.format(kase))
    
    n = int(line)
    distinct = [int(input()) for _ in range(n)]
    # print(distinct)
    
    m = int(input())
    # queries
    for _ in range(m):
        # input()
        query = int(input())
        answer = find_pair(sorted(distinct), len(distinct), query)
        print('Closest sum to {0} is {1}.'.format(query, answer))