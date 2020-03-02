from random import randint


def generate_nearly_ordered_array(n, swap_times):
    arr = []
    for i in range(n):
        arr.append(i)
    for i in range(swap_times):
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        arr[x], arr[y] = arr[y], arr[x]
    return arr


def generate_random_array(n):
    return [randint(0, n) for x in range(n)]


def generate_random_repeat_array(n):
    return [randint(0, 10) for x in range(n)]
