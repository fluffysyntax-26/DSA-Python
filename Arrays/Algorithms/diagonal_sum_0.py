def diagonal_sum(matrix):
    diagonal = 0
    total = 0
    
    for i in range(len(matrix)): 
        total += matrix[i][diagonal]
        print(i, diagonal)
        diagonal += 1
        
    return total

# a better approach
def diagonal_sum(matrix): 
    total = 0
    
    for i in range(len(matrix)): 
        total += matrix[i][i]

    return total