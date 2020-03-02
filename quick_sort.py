from random import randint
import time
import sys

from genera_array import generate_random_repeat_array, generate_random_array, generate_nearly_ordered_array
from swaps import swaps
from insertion_sort import insertion_sort

sys.setrecursionlimit(1000000)


def quick_sort(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)
    quick_sort(arr, l, p - 1)
    quick_sort(arr, p + 1, r)


def partition(arr, l, r):
    v = arr[l]
    # arr[l + 1...j] < v; arr[j + 1...i) > v
    j = l
    for i in range(l + 1, r + 1):
        if arr[i] < v:
            swaps(arr, j + 1, i)
            j += 1
    swaps(arr, j, l)
    return j


def quick_sort_random(arr, l, r):
    if l >= r:
        return
    # if r - l <= 15:
    #     insertion_sort(arr)
    #     return
    p = partition_random(arr, l, r)
    quick_sort_random(arr, l, p - 1)
    quick_sort_random(arr, p + 1, r)


def partition_random(arr, l, r):
    swaps(arr, l, randint(l, r))
    v = arr[l]
    # arr[l + 1...j] < v; [j + 1...i) > v
    j = l
    for i in range(l + 1, r + 1):
        if arr[i] < v:
            j += 1
            swaps(arr, j, i)
    swaps(arr, j, l)
    return j


def quick_sort_two_ways(arr, l, r):
    if r - l <= 15:
        insertion_sort(arr)
        return
    p = partition_two_ways(arr, l, r)
    quick_sort_two_ways(arr, l, p - 1)
    quick_sort_two_ways(arr, p + 1, r)


def partition_two_ways(arr, l, r):
    swaps(arr, l, randint(l, r))
    v = arr[l]
    # arr[l + 1...i) < v; arr(j...r] > v
    i = l + 1
    j = r
    while i <= j:
        while arr[i] < v and i <= r:
            i += 1
        while arr[j] > v and j >= l + 1:
            j -= 1
        swaps(arr, i, j)
        i += 1
        j -= 1
    swaps(arr, l, j)
    return j


def quick_sort_three_ways(arr, l, r):
    if r - l <= 15:
        insertion_sort(arr)
        return
    lt, gt = partition_three_ways(arr, l, r)
    quick_sort_three_ways(arr, l, lt - 1)
    quick_sort_three_ways(arr, gt, r)


def partition_three_ways(arr, l, r):
    swaps(arr, l, randint(l, r))
    v = arr[l]
    # arr[l+1...lt] < v
    lt = l
    # arr[gt...r] > v
    gt = r + 1
    # arr[lt+1...i) == v
    i = l + 1
    while i < gt:
        if arr[i] < v:
            swaps(arr, i, lt)
            i += 1
            lt += 1
        elif arr[i] > v:
            swaps(arr, i, gt - 1)
            gt -= 1
        else:
            i += 1
    swaps(arr, l, lt)
    return lt, gt


# arr = generate_random_array(30)
# quick_sort_three_ways(arr, 0, len(arr) - 1)
# print(arr)
random_arr = generate_random_array(5000)
nearly_random_arr = generate_nearly_ordered_array(5000, 10)
repeat_random_arr = generate_random_repeat_array(5000)
repeat_random_arr1 = repeat_random_arr[:]
# start_first = time.time()
# quick_sort(random_arr, 0, len(random_arr) - 1)
# end_first = time.time()
start_second = time.time()
quick_sort(nearly_random_arr, 0, len(nearly_random_arr) - 1)
end_second = time.time()
start_third = time.time()
quick_sort_random(nearly_random_arr, 0, len(nearly_random_arr) - 1)
end_third = time.time()
# start_four = time.time()
# quick_sort_three_ways(repeat_random_arr, 0, len(repeat_random_arr) - 1)
# end_four = time.time()
# start_two_ways = time.time()
# quick_sort_two_ways(repeat_random_arr1, 0, len(repeat_random_arr1) - 1)
# end_two_ways = time.time()
# print(f'无序数组普通快速排序耗时:\n{end_first - start_first}s')
print(f'近乎有序普通数组快速排序耗时:\n{end_second - start_second}s')
print(f'近乎有序数组使用随机快速排序耗时:\n{end_third - start_third}s')
# print(f'大量重复值数组使用三路快速排序耗时:\n{end_four - start_four}s')
# print(f'大量重复值数组使用双路快速排序耗时:\n{end_two_ways - start_two_ways}s')
