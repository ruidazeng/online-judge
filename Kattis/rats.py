# @ruidazeng
def rats(number):
    tmp = int(str(number)[::-1])
    tmp += number
    return int(''.join(sorted(str(tmp))))

def creepy_checker(string):
    if str_compute[:4] == '1233' and str_compute[-4:] == '4444':
        for char in str_compute[4:-4]:
            if char != '3':
                return False
        return True
    
    if str_compute[:4] == '5566' and str_compute[-4:] == '7777':
        for char in str_compute[4:-4]:
            if char != '6':
                return False
        return True

T = int(input())
for _ in range(T):
    K, M, init = map(int, input().split())
    
    # reinit some variables for each case 
    printed = False
    lst = []
    compute = init
    
    for index in range(1, M + 1):
        
        # check for creeper or repeat
        if compute in lst:
            print(K, 'R', index)
            printed = True
            break
        
        # string of compute (for creeper)
        str_compute = str(compute)
        
        # in case of continum  
        lst.append(compute)
        # new compute = rats(compute)
        last = compute # in case of breaks
        compute = rats(last)
        
        # if less than 8, useless 
        if len(str_compute) < 8:
            continue
        
        if creepy_checker(str_compute):
            print(K, 'C', index)
            printed = True
            break
            
         
    if not printed:
        # print
        print(K, last)