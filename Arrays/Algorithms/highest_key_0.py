# find the key with maximum value in the dictionary

def max_key(my_dict: dict) -> dict: 
    highest_value = 0
    highest_key = None

    for key, value in my_dict.items(): 
        if value > highest_value: 
            highest_value = value
            highest_key = key

    return highest_key

my_dict = {'a': 5, 'b': 9, 'c': 2, 'd':100}
print(max_key(my_dict))