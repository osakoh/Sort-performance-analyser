import random


def bubble_sort(arr):
    c_arr = arr.copy()
    swap = True  # so it runs at least once

    while swap:
        swap = False  # prevents the loop doesn't run infinitely

        for num in range(0, len(c_arr) - 1):
            if c_arr[num] > c_arr[num + 1]:
                swap = True
                c_arr[num], c_arr[num + 1] = c_arr[num + 1], c_arr[num]
    return c_arr


def insertion_sort(arr):
    c_arr = arr
    swap = True  # so it runs at least once

    while swap:
        swap = False  # prevents the loop doesn't run infinitely
        for index in range(1, len(c_arr)):
            # arr[index]- the current value in the array
            current = c_arr[index]
            # index - 1 because the previous line makes current to be a value in the array rather than an index
            previous = index - 1

            if current < c_arr[previous]:
                swap = True
                # shift the larger number to its right and the smaller number to previous
                c_arr[previous + 1], c_arr[previous] = c_arr[previous], current

            current = index + 1
            previous = current - 1

    return c_arr


def merge(arr1, arr2):
    """
    first and second list are sorted in ascending order
    function returns a sorted merged list
    """
    i = j = 0
    merged_list = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_list.append(arr1[i])
            i += 1
        else:
            merged_list.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_list.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_list.append(arr2[j])
        j += 1

    return merged_list


def merge_sort(arr):
    """
    takes an array; keep dividing the arr until it remains one item in the arr and returns it
    returns a sorted array
    """
    # base case for recursion
    if len(arr) < 2:  # 1 element
        return arr

    else:
        midpoint = len(arr) // 2  # integer division
        left = arr[:midpoint]
        right = arr[midpoint:]

        l1 = merge_sort(left)
        l2 = merge_sort(right)
    return merge(l1, l2)


def quick_sort(arr):
    # base case
    if len(arr) < 1:
        return arr

    pivot = random.randint(0, len(arr) - 1)
    left, middle, right = [], [], []

    for num in range(0, len(arr)):
        if arr[num] < arr[pivot]:
            left.append(arr[num])
        elif arr[num] == arr[pivot]:
            middle.append(arr[num])
        else:
            right.append(arr[num])
    # return left, middle, right
    return quick_sort(left) + middle + quick_sort(right)


# print(quick_sort([29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]))
