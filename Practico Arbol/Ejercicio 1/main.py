from arbol import Arbol


if __name__ == '__main__':
    arbol = Arbol()
    arbol.insertar(arbol.getRaiz(),4)
    arbol.insertar(arbol.getRaiz(), 6)
    arbol.insertar(arbol.getRaiz(), 2)
    arbol.insertar(arbol.getRaiz(), 8)
    arbol.insertar(arbol.getRaiz(), 5)
    arbol.insertar(arbol.getRaiz(), 7)
    print('Nivel: {}'.format(arbol.nivel(arbol.getRaiz(), 7)))