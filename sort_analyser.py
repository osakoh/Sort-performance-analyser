import random
import time

from sort_functions import *


def random_list_generator(size, max_num):
    """
    :param size: the list size
    :param max_num: the maximum num to be generated
    :return:
    """
    # gen_list = []
    # for num in range(size):
    #     gen_list.append(random.randint(1, max_num))

    return [random.randint(1, max_num) for _ in range(size)]


def select_function(choice):
    """
    :param choice: an integer value to select a sorting algorithm
    :return: a an object of a sorting algorithm, i.e it doesn't call the function
    """
    if choice == 1:
        return bubble_sort
    elif choice == 2:
        return insertion_sort
    elif choice == 3:
        return merge_sort
    elif choice == 4:
        return quick_sort
    elif choice == 5:
        return sorted
    elif choice == 6:
        return [sorted, bubble_sort, insertion_sort, merge_sort, quick_sort]


def measure_runtime(func, arr):
    """
    :param func: function object without the brackets, i.e the function is not being called
    :param arr:
    :return:
    """
    start = time.time()
    func(arr)
    end = time.time()
    fn = func.__name__.replace("_", " ").title()
    val = round((end - start), 7)
    print(f"  Runtime for {fn}: {val} seconds                    \n"
          f"-----------------------------------------------------\n")
