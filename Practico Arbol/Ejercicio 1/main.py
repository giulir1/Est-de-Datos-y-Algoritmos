from arbol import Arbol


if __name__ == '__main__':
    arbol = Arbol()
    arbol.insertar(arbol.getRaiz(),4)
    arbol.insertar(arbol.getRaiz(), 6)
    arbol.insertar(arbol.getRaiz(), 2)
    arbol.insertar(arbol.getRaiz(), 8)
    arbol.insertar(arbol.getRaiz(), 5)
    arbol.insertar(arbol.getRaiz(), 7)
    arbol.insertar(arbol.getRaiz(), 1)
    arbol.insertar(arbol.getRaiz(), 12)
    arbol.insertar(arbol.getRaiz(), 11)
    arbol.insertar(arbol.getRaiz(), 10)
    arbol.insertar(arbol.getRaiz(), 9)
    if arbol.buscar(arbol.getRaiz(), 7) is not None:
        print('El elemento 7 está en el arbol.')
    #print('Nivel: {}'.format(arbol.nivel(arbol.getRaiz(), 8)))
    #print(arbol.esHoja(arbol.getRaiz(), 4))
    #print(arbol.esHijo(arbol.getRaiz(), 7, 8))
    #print(arbol.esPadre(arbol.getRaiz(), 4, 2))
    #print(arbol.altura(arbol.getRaiz()))
    #arbol.preOrden(arbol.getRaiz())
    print('Camino del nodo x al nodo x: {}'.format(arbol.camino(6, 11)))
