b, br, bs, a, ass = map(int, input().split())

bobMoney = (br - b) * bs
aliceMoney = 0 

while aliceMoney <= bobMoney:
    aliceMoney += ass
    a += 1

print(a)