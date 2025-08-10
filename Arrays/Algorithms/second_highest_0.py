arr = [1, 7, 3, 4, 9, 5] 

def second_highest(arr):
    highest = 0
    higher = 0
    
    for i in arr: 
        if i > highest: 
            higher = highest
            highest = i

        elif i > higher and i < highest: 
            higher = i
        
    return (highest * higher)

print(second_highest(arr))