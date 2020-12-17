
import math
from itertools import combinations

def solution(num_buns,num_required):

    all_keys = []
    buns_list = []
    result = []

    # Part 1: Find minimum number of locks
    
    # Each combination of (num_required-1) bunnies should have 1 unique lock that is not unlockable, and any of the remaining bunnies would have the key to this lock
    ## nCr = n!/(r!(n-r)!)
    num_locks = int(math.factorial(num_buns)/(math.factorial(num_required) * math.factorial(num_buns-num_required)))   
    

    # After selecting any group consisting of (num_required-1) bunnies, the remaining bunnies will each have the key to this lock, as any group 
    # consisting of num_required bunnies must be able to unlock all locks

    # List of all type of keys to be distributed
    for key in range(num_locks):
        all_keys.append(key)
            

    # Part 2: Distribute keys such that the distribution is lexicographically least and no (num_required-1) bunnies can unlock all locks
    
    ## bun_dict.keys() refers to index of bunnies, bun_dict.values() refers to keys being distributed to the bunny of this index 
    bun_dict = {} 
    for bun in range(num_buns):
        bun_dict[bun] = []
    for bun in range(num_buns):
        buns_list.append(bun)

    ## Reversed ordered list of possible combinations of groups consisting of (num_required-1) bunnies (Reversed to ensure that keys appended to each is in ascending order, no sorting required at the end)
    combi = list(reversed(list(combinations(buns_list,num_required-1)))) 
    #print(combi)
    
    ## Lock no. will iterate over number of elements in combi as this is equivalent to number of locks in total
    lock = 0          
    
    ## grp represents the index of bunnies that must not have the key to this current lock
    for grp in combi:  
        for bun in bun_dict:
            if bun not in list(grp):
                bun_dict[bun].append(lock) ## only distribute the key to bunnies not within grp
        lock += 1
    for bun in bun_dict.values():
        result.append(bun)
        
    return result
    
    

# print(solution(1,1))
print(solution(5,3))
# print(solution(4,4))
