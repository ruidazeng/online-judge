# @ruidazeng

def main():
    _ = int(input())
    listy = [int(x) for x in input().split()]

    max_left = -2147483647 # smallest 32-bit signed integers
    min_right = 2147483647 # largest 32-bit signed integers
    pivots = []
    candidates = []

    for left_iter in listy:
        if left_iter > max_left:
            pivots.append(left_iter)
            max_left = left_iter

        
    for right_iter in listy[::-1]:
        if right_iter < min_right:
            candidates.append(right_iter)
            min_right = right_iter

    # Common elements comparison between 2 lists (fast)
    common = list(set(pivots).intersection(candidates))
    print(len(common))

if __name__ == '__main__':  
    main()