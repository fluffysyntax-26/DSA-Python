
# Brute force O(n^2)
def pair_sum(arr, target): 
    for idx1, i in arr: 
        for idx2, j in arr: 
            if (i + j) == target: 
                return (idx1, idx2)
    return (-1, -1)

# Optimised via hashmap/dictionary
def pair_sum_optimised(arr, target): 
    seen = {}

    for i, num in enumerate(arr): 
        complement = target - num

        if complement in seen: 
            return [seen[complement], i]
        seen[num] = i

        
