"""Código para ejemplo de factorial """


def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":

    number = int(input('Ingresa el número para calcular: \n'))

    while number < 0:
        print('El número debe ser positivo.')
        break
    else:
        result = factorial(number)
        print(f'El factorial de {number} es : {result}')
