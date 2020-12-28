from sort_analyser import random_list_generator, measure_runtime, select_function
from sort_functions import *


def menu():
    print("-------------------------- Welcome to my sorting algorithm analyser --------------------------|\n")
    select_options()

    user_input = int(input("Enter option: "))
    size = int(input("\nEnter the size of list to be created: "))
    maximum_num = int(input("Enter the maximum number to be created in the list: "))
    print()
    run = select_function(user_input)  # returns a sort function object

    while user_input != 0:
        if user_input == 1:  # bubble sort
            gen_list = random_list_generator(size, maximum_num)  # generates array
            return measure_runtime(run, gen_list)

        elif user_input == 2:  # insertion sort
            gen_list = random_list_generator(size, maximum_num)  # generates array
            return measure_runtime(run, gen_list)

        elif user_input == 3:  # merge sort
            gen_list = random_list_generator(size, maximum_num)  # generates array
            return measure_runtime(run, gen_list)

        elif user_input == 4:  # quick sort
            gen_list = random_list_generator(size, maximum_num)  # generates array
            return measure_runtime(run, gen_list)

        elif user_input == 5:  # python's sorting function
            gen_list = random_list_generator(size, maximum_num)  # generates array
            return measure_runtime(run, gen_list)

        elif user_input == 6:  # save user profile
            gen_list = random_list_generator(size, maximum_num)  # generates array
            for functions in run:
                res = measure_runtime(functions, gen_list)
            return res

        select_options()  # display a list of options for the user to choose from
        user_input = int(input("\nSelect from the menu: "))
        gen_list = random_list_generator(size, maximum_num)  # generates array


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


if __name__ == '__main__':
    menu()
