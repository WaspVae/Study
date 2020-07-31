def binary_search(arr, n, item):
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1
