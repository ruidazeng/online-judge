# function to generate all the sub lists 
def sub_lists(list1): 
  
    # store all the sublists  
    sublist = [[]] 
      
    # first loop  
    for i in range(len(list1) + 1): 
          
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
              
            # slice the subarray  
            sub = list1[i:j] 
            sublist.append(sub) 
              
      
    return sublist 

end, length = map(int, input().split())

room = [int(x) for x in input().split()]
room.append(end)

# new list track distance in between
dist = list()
prev = 0
for num in room:
    temp = num - prev 
    dist.append(temp)
    prev = num


# storage
result = list()

for sublist in sub_lists(dist):
    # each combinations
    if len(sublist) != 0:
        result.append(sum(sublist))

# preserve unique
print(*sorted(set(result)))