N = int(input())
papers = [int(x) for x in input().split()]

# check possible or nah
tracker = 0
for index, pap in enumerate(papers[::-1]):
    tracker += pap * (2 ** index)

if tracker < (2 ** (N - 1)):
    print('impossible')
    quit()

# calculate connecting length
start_length = 2 ** (-5/4)
start_width = 2 ** (-3/4)
tape = 0

# find A-N paper length and width (break down)
for i in range(N):
    if i%2 == 0:
        start_width /= 2
    else:
        start_length /= 2

# calculate a needed paper list
needed_papers = [0 for _ in range(N)]
needed_papers[0] = 2
for index, pap in enumerate(papers):
    # if fulfilled, stop
    if pap >= needed_papers[index]:
        # needed_papers[index]
        break
    
    # else move on
    needed_papers[index + 1] += (needed_papers[index] - pap) * 2
    needed_papers[index] = pap
    
# print(needed_papers)      
    
# tracing back
next_level = 0
for index in reversed(range(len(needed_papers))):
    # reverse traversal
    pap = needed_papers[index]
    if pap == 0: continue
    
    needed = pap // 2
    # if A even: width, if odd: length
    if (index + 2) % 2 == 0:
        tape += needed * start_width
        start_length *= 2
    else:
        tape += needed * start_length
        start_width *= 2
    needed_papers[index - 1] += needed
    
print(2 * tape)