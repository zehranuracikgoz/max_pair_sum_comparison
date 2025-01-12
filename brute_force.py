def find_max_sum_indices(arr):
    max_sum = 0 
    index1, index2 = 0, 0 

    
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            current_sum = arr[i] + arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                index1, index2 = i, j

    return index1, index2, max_sum