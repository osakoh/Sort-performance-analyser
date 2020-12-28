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


def select_options():
    print("____________________________________\n"
          "| 1.     Bubble sort               |\n"
          "| 2.     Insertion sort            |\n"
          "| 3.     Merge sort                |\n"
          "| 4.     Quick Sort                |\n"
          "| 5.     Python's sorted Function  |\n"
          "| 6.     Run all function          |\n"
          "| 0.     Exit application          |\n"
          "|__________________________________|")


def select_function(choice):
    select_options()
    choice = int(input("Select algorithm to run: "))

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
        temp = [bubble_sort, insertion_sort, merge_sort, quick_sort, sorted]
        return temp
    else:
        exit()


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
    print(f"\nRuntime for {fn}: {end - start} seconds")


