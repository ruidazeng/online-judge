N = int(input())

for _ in range(N):
    cmd = input()
    if "Simon says" in cmd:
        print(cmd[10:])