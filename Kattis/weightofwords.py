l, w = map(int, input().split())

abc = {1:'a',
2:'b',
3:'c',
4:'d',
5:'e',
6:'f',
7:'g',
8:'h',
9:'i',
10:'j',
11:'k',
12:'l',
13:'m',
14:'n',
15:'o',
16:'p',
17:'q',
18:'r',
19:'s',
20:'t',
21:'u',
22:'v',
23:'w',
24:'x',
25:'y',
26:'z'}

if w < l:
    print('impossible')

elif w > l*26:
    print('impossible')

else:
    a = [1]*l
    temp = 0
    if sum(a) != w: 
        for i in range(len(a)):
            for j in range(25):
                a[i] = a[i] + 1
                temp = sum(a)
                if temp == w:
                    break
            if temp == w:
                break
    for i in range (len(a)):
        print(abc[a[i]],end='')