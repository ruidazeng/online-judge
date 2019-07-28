K = int(input())
my_answer = input()
friend_answer = input()
total_q = len(my_answer)
same = 0

for x, y in zip(my_answer, friend_answer):
    if x == y:
        same += 1
difference = total_q - same
if same >= K:
    print(K + difference)
else:
    print(same + total_q - K)