from listaSecuencial import ListaSecuencial

if __name__ == '__main__':
    lista = ListaSecuencial(5)
    lista.crear()
    lista.insertar(0, 1)
    lista.insertar(1, 2)
    lista.insertar(2, 3)
    lista.insertar(1, 55)
    lista.suprimir(1)