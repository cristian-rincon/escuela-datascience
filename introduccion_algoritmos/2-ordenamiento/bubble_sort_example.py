# 1. Comparación de los elementos adyacentes
# 2. Repetir hasta tener un set completo sin saltos
import random


def change_pos(n1: int, n2: int):

    temp = n1
    n1 = n2
    n2 = temp

    return n1, n2


def bubble_sort(ingress_vector):
    n = len(ingress_vector)

    for i in range(n):
        for j in range(n - i - 1):
            if ingress_vector[j] > ingress_vector[j + 1]:
                ingress_vector[j], ingress_vector[j + 1] = ingress_vector[j + 1], ingress_vector[j]


def print_numbers(ingress_vector):

    n = len(ingress_vector)

    for i in range(n):
        print(f'{i}')


if __name__ == "__main__":

    welcome = """
    ,---.     |    |    |                            |
    |---..   .|---.|---.|    ,---.    ,---.,---.,---.|---
    |   ||   ||   ||   ||    |---'    `---.|   ||    |
    `---'`---'`---'`---'`---'`---'    `---'`---'`    `---'
    """

    print(welcome)
    print('¡Welcome to Bubble Sort program! \n')
    numbers = int(input('¿How many numbers you want to sort? '))
    numbers_list = [x for x in range(numbers)]
    random.shuffle(numbers_list)
    print('Before')
    print(*numbers_list)

    print('After')
    bubble_sort(numbers_list)
    print(*numbers_list)
