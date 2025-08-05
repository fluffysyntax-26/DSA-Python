from array import * 

def linear_search(array, key): 
    for idx, ele in enumerate(array): 
        if key == ele: 
            return idx
    return -1

array1 = array('i', [10,20,30,40,50,60])
key = int(input("Enter an element to search for in the array: "))

result = linear_search(array1, key)

if result == -1:
    print("Element not found")
else: 
    print(f"Element found at index {result}") 
    

   