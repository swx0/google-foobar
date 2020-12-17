
def generateBinaryStrings(n,possiblePermutations, string = ''):
    if n > 0:
        generateBinaryStrings(n-1,possiblePermutations, string + '0')
        generateBinaryStrings(n-1,possiblePermutations, string + '1')
    else:
        possiblePermutations[string] = 1
    
def generateBinaryStrings2(n,possibleBinaryStrings,string=''):
    if n > 0:
        generateBinaryStrings2(n-1, possibleBinaryStrings, string + '0')
        generateBinaryStrings2(n-1, possibleBinaryStrings, string + '1')
    else:
        possibleBinaryStrings.append(string)

def solution(current):
    
    # binString.keys() represent the binary strings computed and binString.values() represent output of the the binary strings after 1 time step    
    binString = {}
    
    # Convert from boolean matrix to binary transpose matrix
    widthInput = len(current[0])
    heightInput = len(current)
    result = []
    for x in range(widthInput):
        temp = ''
        for y in range(heightInput):
            temp += str(int(current[y][x]))
        result.append(temp)
        
    current = result

    count = 0
    height = heightInput +1
    
    # Generate a list of permutations of binary strings with length equal to height variable
    possibleBinaryStrings = []
    generateBinaryStrings2(height,possibleBinaryStrings)
    
    for currentColumn in range(len(current)):
        overlapList = {}
       
        # For the first column
        if count == 0: 
            possiblePermutations = {}
            # Generate all permutations of the first column
            generateBinaryStrings(height,possiblePermutations)      
            count += 1       

        
        # Check permutations that satisfy the currentColumn (using pointers)
        for possible1 in possiblePermutations: 
            for possible2 in possibleBinaryStrings:
                possibleHash = (possible1,possible2)
                
                if possibleHash in binString:
                    check = binString[possibleHash]
    
                else:
                    point1 = 0
                    point2 = 1
                
                    check = ''
                    while point2 < height: 
                        if int(possible1[point1]) + int(possible1[point2]) + int(possible2[point1]) + int(possible2[point2]) == 1:
                            check += '1'
                        else:
                            check += '0'
                        point1 += 1
                        point2 += 1
                
                    # Add a binary string entry to binString
                    binString[possibleHash] = check  
                    
                if check == current[currentColumn]:
                    
                    # Take the tail of the previous column as the head of the next column
                    head = possible2  
                    
                    # Keep track of the counts associated with permutations that satisfy currentColumn
                    if head not in overlapList:
                        overlapList[head] = possiblePermutations[possible1]
                    else:
                        overlapList[head] += possiblePermutations[possible1]


        # print('overlap list:',overlapList)
        # print()
        
        possiblePermutations = overlapList
            
        # print('possible permutations:',possiblePermutations)
    return (sum(overlapList.values()))
        

 


# g = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]

g = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]

# g = [[True, False, True], [False, True, False], [True, False, True]]

print(solution(g))

