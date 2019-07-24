N = int(input())

for _ in range(N):
    prob = input()
    if prob == "P=NP":
        print("skipped")
    else:
        a, b = map(int, prob.split("+"))
        print(a + b)
        
        # print(eval(prob)) also works...