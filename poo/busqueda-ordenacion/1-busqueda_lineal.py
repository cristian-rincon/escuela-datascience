import random


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break


if __name__ == "__main__":
    tamano_de_lista = int(input('¿De qué tamaño será la lista? \n'))
    objetivo = int(input('¿Qué número quieres encontrar? \n'))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)

    print('La lista de números es:')
    print(lista)
    print(
        f'El número {objetivo} {"está" if encontrado else "no está"} en la lista')
