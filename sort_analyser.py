import random


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


print(random_list_generator(5, 100))
