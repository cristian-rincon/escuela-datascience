def reverse_string(input_string):

    if not len(input_string):
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]


if __name__ == "__main__":

    input_string = input('¿Cual es la cadena que quieres reordenar? \n')

    print(reverse_string(input_string))
