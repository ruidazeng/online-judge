N = int(input())

for _ in range(N):
    
    result = True
    
    # tracker
    money = 0
    incense = 0
    gem = 0
    last = None
    
    stack = []
    line = input()
    
    
    for char in line:
        if char == '.':
            continue
        elif char == '$':
            money += 1
            stack.append('$')
        elif char == '|':
            incense += 1 
            stack.append('|')
        elif char == '*':
            gem += 1
            stack.append('*')
        elif char == 't':
            if incense == 0 or stack[-1] != '|':
                result = False
                break
            else:
                incense -= 1
                stack.pop()
        # print('shit')
        elif char == 'j':
            if gem == 0 or stack[-1] != '*':
                result = False
                break
            else:
                gem -= 1
                stack.pop()
        # print('shit')
        elif char == 'b':
            # print(money)
            # print('shit')
            if money == 0 or stack[-1] != '$':
                result = False
                # print('shit')
                break
            else:
                money -= 1 
                stack.pop()
    
    if money or incense or gem:
        result = False
        # print('shit')
        
    if result:
        print('YES')
    else:
        print('NO')