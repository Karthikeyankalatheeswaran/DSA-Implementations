def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index where found
    return -1   # not found