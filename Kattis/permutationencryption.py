import math
while True:
    num_crunch = [int(x) for x in input().split()]
    
    if num_crunch == [0]:
        break
    
    div = num_crunch.pop(0)
    toberead = input()
    
    # adjust length for spaces at the end
    tobe_len = len(toberead)
    new_len = math.ceil(tobe_len/div) * div
    toberead = toberead.ljust(new_len)
    
    print('\'', end = '')
    
    for index in range(new_len):
        print(toberead[ (num_crunch[index%div] - 1) + index//div * div ], end = '')
    print('\'')