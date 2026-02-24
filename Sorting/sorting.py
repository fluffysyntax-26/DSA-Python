def bubble_sort(custom_list): 
    for i in range(len(custom_list) - 1): 
        for j in range(len(custom_list) - i - 1): 
            # swap
            if custom_list[j] > custom_list[j + 1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]

    return custom_list

def selection_sort(arr): 
    for i in range(len(arr)): 
        min_index = i
        for j in range(i+1, len(arr)): 
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        pass


if __name__ == "__main__":
    custom_list = [19, 89, 20, 34, 20, 19, 23, 67, 81]
    print(bubble_sort(custom_list))
    print(selection_sort(custom_list))