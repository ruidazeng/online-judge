# put in list 
import sys

lst = list()
for line in sys.stdin:
    line = line.replace('\n', '')
    lst.append(line)

ragged = 0
offset = len(max(lst, key=len))

for x in lst[:-1]:
    ragged += (offset - len(x)) ** 2

print(ragged)