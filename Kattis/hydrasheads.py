while True:
    h, t = map(int, input().split())
    
    if h == 0 and t == 0:
        break
        
    # Impossible if odd num of heads and no tails.
    elif h % 2 == 1 and t == 0:
        print(-1)
        
    # Head cannot be odd after eliminating the tails.
    elif h % 2 == 0: # Even initial heads
        add_tail = (4-t)%4
        moves = (h+(t+add_tail)//2)//2 + add_tail + (t+add_tail)//2
        print(moves)
    
    elif h % 2 == 1: # Odd initial heads
        add_tail = (4-(2+t))%4
        moves = (h+(t+add_tail)//2)//2 + add_tail + (t+add_tail)//2
        print(moves)