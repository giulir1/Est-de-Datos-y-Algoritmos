from pilaSecuencial import PilaSecuencial


def decimalABinario(decimal):
    pila = PilaSecuencial(8)
    band = False
    while not band:
        resto = decimal % 2
        decimal = decimal // 2
        pila.insertar(resto)
        if decimal == 0:
            band = True
        return pila

    if __name__ == '__main__':
        try:
            num = int(input('Ingrese un numero entero: '))
            pila = decimalABinario(num)
            pila.mostrar()
        except ValueError:
            print('ERROR - Debe ingresar un numero entero.')