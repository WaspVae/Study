import time
import sys

from insertion_sort import insertion_sort

sys.setrecursionlimit(1000000)


def merge_sort1(arr):
    # if len(arr) <= 1:
    #     return arr
    if len(arr) <= 15:
        insertion_sort(arr)
        return arr
    mid = len(arr) // 2
    left = merge_sort1(arr[:mid])
    right = merge_sort1(arr[mid:])
    if arr[:mid][-1] > arr[mid:][0]:
        return merge(left, right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # if len(arr) <= 15:
    #     insertion_sort(arr)
    #     return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # if arr[:mid][-1] > arr[mid:][0]:
    return merge(left, right)


def merge(left, right):
    # result = []
    # while left and right:
    #     if left[0] <= right[0]:
    #         result.append(left.pop(0))
    #     else:
    #         result.append(right.pop(0))
    # if left:
    #     result += left
    # if right:
    #     result += right
    # return result
    # 双指针
    l = len(left)
    r = len(right)
    i = j = 0
    res = []
    while i < l and j < r:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < l:
        res.extend(left[i:])
    if j < r:
        res.extend(right[j:])
    return res


from genera_array import generate_random_array, generate_nearly_ordered_array, generate_random_repeat_array
from quick_sort import quick_sort, quick_sort_random, quick_sort_two_ways, quick_sort_three_ways

random_arr = generate_random_array(5000)
nearly_random_arr = generate_nearly_ordered_array(100000, 10)
repeat_random_arr = generate_random_repeat_array(5000)
repeat_random_arr1 = repeat_random_arr[:]
# start_first = time.time()
# quick_sort(random_arr, 0, len(random_arr) - 1)
# end_first = time.time()
# start_second = time.time()
# quick_sort(nearly_random_arr, 0, len(nearly_random_arr) - 1)
# end_second = time.time()
# start_third = time.time()
# quick_sort_random(random_arr, 0, len(random_arr) - 1)
# end_third = time.time()
start_four = time.time()
quick_sort_three_ways(repeat_random_arr, 0, len(repeat_random_arr) - 1)
end_four = time.time()
start_two_ways = time.time()
quick_sort_two_ways(repeat_random_arr1, 0, len(repeat_random_arr1) - 1)
end_two_ways = time.time()
# start_merge = time.time()
# merge_sort1(repeat_random_arr1)
# end_merge = time.time()
# print(f'无序数组普通快速排序耗时:\n{end_first - start_first}s')
# print(f'近乎有序普通数组快速排序耗时:\n{end_second - start_second}s')
# print(f'近乎有序数组使用随机快速排序耗时:\n{end_third - start_third}s')
print(f'大量重复值数组使用三路快速排序耗时:\n{end_four - start_four}s')
print(f'大量重复值数组使用双路快速排序耗时:\n{end_two_ways - start_two_ways}s')
# print(f'大量重复值数组使用归并排序耗时:\n{end_merge - start_merge}s')
