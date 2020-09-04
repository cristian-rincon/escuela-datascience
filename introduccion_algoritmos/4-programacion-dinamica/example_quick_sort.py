def quick_sort(lista):
    """ Ordena la lista de forma recursiva.
        Pre: los elementos de la lista deben ser comparables.
        Devuelve: una nueva lista con los elementos ordenados. """

    # Caso base
    if len(lista) < 2:
        return lista
    # Caso recursivo
    menores, medio, mayores = _partition(lista)
    return quick_sort(menores) + medio + quick_sort(mayores)


def _partition(lista):
    """ Pre: lista no vacía.
        Devuelve: tres listas: menores, medio y mayores. """

    pivote = lista[0]
    menores = []
    mayores = []
    for x in range(1, len(lista)):
        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    return menores, [pivote], mayores


if __name__ == "__main__":
    lista_desordenada = [3 ,94 ,86 ,82 ,90,10 ,87 ,36 ,61 ,8,17 ,15 ,22 ,10,23]
    lista_ordenada =  []
        
    for i in quick_sort(lista_desordenada):
        lista_ordenada.append(i)
    
    print(f'La lista inicial es: \n {lista_desordenada}')
    print(f'La lista ordenada es: \n {lista_ordenada}')
