n = int(input())

n = bin(n)[2:] # [0:2] = '0b'
revBin = n[::-1]
nBin = int(revBin, 2)

print(nBin)