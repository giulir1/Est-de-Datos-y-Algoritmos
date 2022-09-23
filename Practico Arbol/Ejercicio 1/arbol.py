from nodo import Nodo

# {}
class Arbol:
    __raiz = None

    def __init__(self):
        self.__raiz = None
    
    def vacio(self, arbol):
        return arbol == None

    def getRaiz(self):
        return self.__raiz

    def mostrarRaiz(self):
        return self.__raiz.getDato()

    def buscar(self, arbol, dato, nivel=0):
        if self.vacio(arbol):
            print('ERROR - Elemento inexistente.')
        else:
            if arbol is not None:
                if arbol.getDato() == dato:
                    print('El dato "{}" se encuentra en el arbol.'.format(dato))
                elif dato < arbol.getDato():
                        arbol = arbol.getIzq()
                        nivel += 1
                        nivel = self.buscar(arbol, dato, nivel)
                else:
                    arbol = arbol.getDer()
                    nivel += 1
                    print('se aumento el nivel: {}'.format(nivel))
                    nivel = self.buscar(arbol, dato, nivel)
        return nivel
    
    def insertar(self, arbol, dato):
        if self.vacio(arbol):
            unNodo = Nodo(dato)
            self.__raiz = unNodo
        else:
            if dato == arbol.getDato():
                print('ERROR - El elemento ya existe en el árbol.')
            elif dato < arbol.getDato():
                if arbol.getIzq() is None:
                    arbol.setIzq(Nodo(dato))
                else:
                    arbol = arbol.getIzq()
                    self.insertar(arbol, dato)
            else:
                if arbol.getDer() is None:
                    arbol.setDer(Nodo(dato))
                else:
                    arbol = arbol.getDer()
                    self.insertar(arbol, dato)

    def nivel(self, arbol, dato):
        nivel = self.buscar(arbol, dato)
        return nivel