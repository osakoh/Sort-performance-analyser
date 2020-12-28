from sort_analyser import random_list_generator, measure_runtime
from sort_functions import *


def menu():
    print("\t\t|--- Welcome to my sorting algorithm analyser ---|\n")
    menu_options()

    user_input = int(input("Enter option: "))
    size = int(input("Enter the size of list to be created: "))
    maximum_num = int(input("Enter the maximum number to be created in the list: "))

    gen_list = random_list_generator(size, maximum_num)

    while user_input != 0:
        if user_input == 1:  #
            print(user_input)

        elif user_input == 2:  #
            print(user_input)

        elif user_input == 3:  #
            print(user_input)

        elif user_input == 4:  # delete a movie
            print(user_input)

        elif user_input == 5:  # show watched movies
            print(user_input)

        elif user_input == 6:  # save user profile
            print(user_input)

        menu_options()  # display a list of options for the user to choose from
        user_input = int(input("Select from the menu: "))


def menu_options():
    print("____________________________________\n"
          "¦____ Movie Rental Application ____¦\n"
          "| 1.     Add a movie               |\n"
          "| 2.     View list of movies       |\n"
          "| 3.     Set a movie as watched    |\n"
          "| 4.     Delete a movie            |\n"
          "| 5.     View watched movies       |\n"
          "| 6.     Save profile              |\n"
          "| 0.     Exit application          |\n"
          "|__________________________________|")


if __name__ == '__main__':
    menu()
