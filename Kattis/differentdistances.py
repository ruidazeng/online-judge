while True:
    n = input()
    if n == '0':
        break
    x1, y1, x2, y2, p = map(float, n.split())
    p_norm = ((abs(x1 - x2))**p + (abs(y1 - y2))**p)**(1/p)
    print(format(p_norm,'.10f'))