from arbol import Arbol


if __name__ == '__main__':
    arbol = Arbol()
    arbol.insertarRaiz(4)
    raiz = arbol.getRaiz()
    arbol.insertar(raiz, 6)
    arbol.insertar(raiz, 1)
    arbol.buscar(raiz, 6)
    #print(arbol.mostrarRaiz())
    