CONTESANTS = 5

# Safer to assign winScore and winIndex 
# to the score/index of first CONTESANTS~
winScore = 0
winIndex = 0

for i in range(CONTESANTS):
    grades = list(map(int, input().split()))
    if sum(grades) > winScore:
        winScore = sum(grades)
        winIndex = i + 1
        
print(winIndex, winScore)