def missing_number(arr, n):
    number = 0
    missing_number = None
    
    for i in arr: 
        number += 1 
        if i != number: 
            missing_number = number

    return missing_number

arr = [9,6,4,2,3,5,7,0,1]

print(missing_number(arr, 6))