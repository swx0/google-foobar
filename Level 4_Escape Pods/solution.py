def solution(entrances,exits,path):
    # Add arbituary source and arbituary sink
    
    ## arbituaryPath refers to n+1 * n+1 matrix, with s and t included
    arbituaryPath = path.copy() 

    arb = [0]*len(path)
    
    ## refers to arbituary source
    arbituaryPath.insert(0,arb)  
    
    ## refers to arbituary sink
    arbituaryPath.append(arb)    
    
    for x in arbituaryPath:
        x.insert(0,0)
        x.append(0)
        
    ## capacity of edges connecting arbituary source to original sources is equal to the total capacity of all outgoing edges from original sources
    for source in entrances:    
        sCap = sum(path[source])
        arbituaryPath[0][source+1] = sCap
        
    ## capacity of edges connecting from original sinks to arbituary sink is equal to the total capacity of all incoming edges to original sinks    
    for sink in exits:    
        tCap = 0
        for room in range(len(path)):
            tCap += path[room][sink+1]
        arbituaryPath[sink+1][-1] = tCap
        
    maxFlow = 0     
        
    # Edmonds-Karp
    Gf = arbituaryPath.copy() # Initialise residual graph Gf
    print(Gf)
    
    queue = [[0]]
    
    ## while there exists an augmenting path from s to t in the residual graph Gf
    while True: 

        augPath = BFS(Gf,queue) # augmenting path found using BFS
        if augPath is None:
            return maxFlow
        print(augPath)
        
        ## p refers to an array of weights of edges in augmenting path, edge weight has to be >0 to exist
        p = []  

        for i in range(len(augPath)):
            if i+1 < len(augPath):
                p.append(Gf[augPath[i]][augPath[i+1]])
        print(p)
        
        ## residual capacity of augmenting path Cf_p
        Cf_p = min(p)  
        maxFlow += Cf_p
        print(maxFlow)
        for i in range(len(augPath)):
            if i+1 < len(augPath):
                ## subtract Cf_p from forward edge
                Gf[augPath[i]][augPath[i+1]] -= Cf_p
                
                ## add Cf_p to backward edge
                Gf[augPath[i+1]][augPath[i]] += Cf_p 
    
    return maxFlow

def BFS(Gf,queue):
    arbituarySink = len(Gf)-1

    while len(queue) > 0:
        current = queue.pop(0)
        if current[-1] == arbituarySink:
            # print(current)
            return current
        for v in range(len(Gf[current[-1]])):
            if v not in current:
                Cf = Gf[current[-1]][v]
                if Cf > 0:
                    copyCurrent = current.copy()
                    copyCurrent.append(v)
                    queue.append(copyCurrent)
                
    return None
                    
                    
                    
                    
entrances = [0, 1]
exits = [4, 5]

path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

# entrances = [0]
# exits = [3]

# path = [[0, 1000000, 1000000, 0], [0, 0, 1, 1000000], [0, 0, 0, 1000000], [0, 0, 0, 0]]


# entrances = [0]
# exits = [5]

# path = [[0, 16, 13, 0, 0, 0], 
#         [0, 0, 10, 12, 0, 0], 
#         [0, 4, 0, 0, 14, 0], 
#         [0, 0, 9, 0, 0, 20], 
#         [0, 0, 0, 7, 0, 4], 
#         [0, 0, 0, 0, 0, 0]] 

print(solution(entrances,exits,path))
