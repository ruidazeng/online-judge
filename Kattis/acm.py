correct = 0
num_wrong = 0
correct = [] # Stores the 
all_problem = {} # Python dictionaries (key: value pairs)
wrong_attempts = {}

while True:
    line = input()
    if line == '-1':
        break
    n, m, rw = line.split()
    n = int(n)

    # Check to see if the answer is right/wrong
    if rw == 'right':
        all_problem[m] = n
        if m not in correct:
            correct.append(m)
    elif rw == 'wrong':
        if m in wrong_attempts:
            wrong_attempts[m] += 1 
        elif m not in wrong_attempts:
            wrong_attempts[m] = 1

total_time = 0
for p in correct:
    total_time += int(all_problem[p])
    if p in wrong_attempts:
        total_time += int(wrong_attempts[p]) * 20

print(len(correct), total_time)