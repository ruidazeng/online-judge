n = input()

good = False
# validity check
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        good = True
        break

if not good:
    print(0)
    quit()

# loop
test = str(int(n) + 1)
while True:
    for num in n:
        continum = False
        # print(num, test, n.count(num), test.count(num))
        if n.count(num) != test.count(num):
            test = int(test)
            test += 1 
            test = str(test)
            continum = True
            break
    if continum: continue
    break

print(test)