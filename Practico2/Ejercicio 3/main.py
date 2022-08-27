from pilaSecuencial import PilaSecuencial


def calculoFactorial(num):
    pila = PilaSecuencial(8)
    pila.crear()
    while num > 0:
        pila.insertar(num)
        num -= 1
    factorial = (pila.factorial())
    return factorial


if __name__ == '__main__':
    try:
        numero = int(input('Ingrese un número entero mayor a 0: '))
        if numero <= 0:
            print('ERROR - Debe ingresar un número mayor a 0.')
        else:
            print('Factorial del número {}: {}'.format(numero, calculoFactorial(numero)))
    except ValueError:
        print('ERROR - Debe ingresar un numero entero.')

