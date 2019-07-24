import queue

cups = queue.PriorityQueue()
n = int(input())

for _ in range(n):
    color, radius = input().split()
    
    try:
        # A typical pattern for entries is
        # a tuple in the form: (priority_number, data).
        cups.put((int(radius), color))
        
    except:
        cups.put((int(color)//2, radius))

while not cups.empty():
    
    # The lowest valued entries are retrieved first
    print(cups.get()[1])