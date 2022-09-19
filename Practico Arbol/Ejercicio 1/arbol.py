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

    def insertarRaiz(self, dato):
        raiz = Nodo(dato)
        self.__raiz = raiz

    def buscar(self, arbol, dato):
        print(arbol.getDato())
        if self.vacio(arbol):
            print('ERROR - Elemento inexistente.')
        else:
            if arbol is not None:
                if arbol.getDato() == dato:
                    print('El dato "{}" se encuentra en el arbol.'.format(dato))
                elif dato < arbol.getDato():
                        arbol = arbol.getIzq()
                        self.buscar(arbol, dato)
                else:
                    arbol = arbol.getDer()
                    self.buscar(arbol, dato)
    
    def insertar(self, arbol, dato):
        if self.vacio(arbol):
            unNodo = Nodo(dato)
        else:
            if dato == arbol.getDato():
                print('ERROR - El elemento ya existe en el árbol.')
            elif dato < arbol.getDato():
                arbol = arbol.getIzq()
                self.insertar(arbol, dato)
            else:
                arbol = arbol.getDer()
                self.insertar(arbol, dato)


    #def insertar(self, x):
    #    if self.vacio():
    #        self.__raiz = Nodo(x)
    #    else:
    #        if self.__raiz.getDato()==x:
    #            print("Elemento ya Existe")
    #        else:
    #            if self.__raiz.getDato() < x:
    #                unNodo = Nodo(x)
    #                self.__raiz.setIzq(unNodo)
    #            else:
    #                unNodo = Nodo(x)
    #                self.__raiz.setDer(unNodo)