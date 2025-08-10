import numpy as np

def linear_search(array: np.array, key: int) -> tuple:
    for row_idx, i in enumerate(array): 
        for idx, ele in enumerate(i): 
            if  ele == key: 
                return (row_idx, idx) 
    return (-1, -1) 

iterable = [[45, 10, 30, 99, 64, 53],
       [79, 91, 24, 13, 45, 41],
       [63, 38, 27, 23, 96, 79],
       [38, 21, 85, 64, 14, 13],
       [67, 21, 37, 39, 74, 87],
       [85, 13, 81, 35, 93, 99],
       [45, 29, 37, 53, 23, 21]]

arr = np.array(iterable, dtype = 'int8')
results = linear_search(arr, key=100)

if results == (-1, -1): 
    print("Element not found")
else: 
    print(f"Element found at [{results[0]}][{results[1]}]")


