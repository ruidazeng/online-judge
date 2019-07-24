A, B, C = input().split()

for oper in ['+', '-', '/', '*']:
    
    expr = A + oper + B + '=' + C
    
    # The exec() method executes the dynamically 
    # created program, which is either a string or a code object.
    
    exec('is_valid = ' + expr.replace('=', '=='))
    if is_valid:
        print(expr)
        break

    expr = A + '=' + B + oper + C
    exec('is_valid = ' + expr.replace('=', '=='))
    if is_valid:
        print(expr)
        break