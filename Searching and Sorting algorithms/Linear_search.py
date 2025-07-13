def linear_search(arr, target):
    # TODO: Implement this function
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
