from pilaSecuencial import PilaSecuencial


if __name__ == '__main__':
    try:
        band = False
        tamano = int(input('Ingrese tamaño de la pila: '))
        pila = PilaSecuencial(tamano)
        pila.crear()
        continuar = int(input('1 - Manejar pilas\n0 - SALIR\nOpción: '))
        while continuar != 0:
            if continuar == 1:
                numPila = int(input('Ingrese numero de pila (1-2): '))
                if numPila == 1:
                    op = int(input('1 - Ingresar numero\n2 - Suprimir número\n3 - Mostrar pila\nOpción: '))
                    if op == 1:
                        num = int(input('Ingrese un número entero a ingresar: '))
                        if not pila.insertarPila1(num):
                            print('ERROR - PILA 1 LLENA\n')
                    elif op == 2:
                        pila.suprimirPila1()
                    elif op == 3:
                        print(pila.mostrarPila1())
                    else:
                        print('ERROR - Ingrese una opción correcta.')
                elif numPila == 2:
                    op = int(input('1 - Ingresar numero\n2 - Suprimir número\n3 - Mostrar pila\nOpción: '))
                    if op == 1:
                        num = int(input('Ingrese un número entero a ingresar: '))
                        if not pila.insertarPila2(num):
                            print('ERROR - PILA 2 LLENA\n')
                    elif op == 2:
                        pila.suprimirPila2()
                    elif op == 3:
                        print(pila.mostrarPila2())
                    else:
                        print('ERROR - Ingrese una opción correcta.')
                else:
                    print('ERROR - Debe seleccionar Pila N°1 o Pila N°2')
            continuar = int(input('1 - Manejar pilas\n0 - SALIR\nOpción: '))
    except ValueError:
        print('ERROR - Debe ingresar un número entero.')
