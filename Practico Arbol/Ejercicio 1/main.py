
from arbol import Arbol


if __name__ == '__main__':
    arbol = Arbol()
    arbol.insertar(arbol.getRaiz(),4)
    arbol.insertar(arbol.getRaiz(), 6)
    arbol.insertar(arbol.getRaiz(), 2)
    arbol.insertar(arbol.getRaiz(), 8)
    arbol.insertar(arbol.getRaiz(), 5)
    arbol.insertar(arbol.getRaiz(), 7)
    #arbol.buscar(arbol.getRaiz(), 7)
    #print('Nivel: {}'.format(arbol.nivel(arbol.getRaiz(), 8)))
    #print(arbol.esHoja(arbol.getRaiz(), 4))
    #print(arbol.esHijo(arbol.getRaiz(), 7, 8))
    #print(arbol.esPadre(arbol.getRaiz(), 4, 2))
    #print(arbol.altura(arbol.getRaiz()))
    arbol.preOrden(arbol.getRaiz())
